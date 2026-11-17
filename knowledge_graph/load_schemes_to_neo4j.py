
import json
import os
import re
from pathlib import Path

from dotenv import load_dotenv
from neo4j import GraphDatabase


# --------------------------------------------------
# 1. Load configuration
# --------------------------------------------------

PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = PROJECT_DIR / "data" / "processed" / "schemes.json"

load_dotenv(PROJECT_DIR / ".env")

NEO4J_URI = os.getenv("NEO4J_URI")
NEO4J_USERNAME = os.getenv("NEO4J_USERNAME")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD")
NEO4J_DATABASE = os.getenv("NEO4J_DATABASE", "neo4j")


# --------------------------------------------------
# 2. Create unique constraints
# --------------------------------------------------

CONSTRAINTS = [
    """
    CREATE CONSTRAINT department_id IF NOT EXISTS
    FOR (n:Department) REQUIRE n.department_id IS UNIQUE
    """,
    """
    CREATE CONSTRAINT scheme_id IF NOT EXISTS
    FOR (n:Scheme) REQUIRE n.scheme_id IS UNIQUE
    """,
    """
    CREATE CONSTRAINT source_id IF NOT EXISTS
    FOR (n:Source) REQUIRE n.source_id IS UNIQUE
    """,
    """
    CREATE CONSTRAINT eligibility_id IF NOT EXISTS
    FOR (n:Eligibility) REQUIRE n.eligibility_id IS UNIQUE
    """,
    """
    CREATE CONSTRAINT benefit_id IF NOT EXISTS
    FOR (n:Benefit) REQUIRE n.benefit_id IS UNIQUE
    """,
    """
    CREATE CONSTRAINT document_id IF NOT EXISTS
    FOR (n:Document) REQUIRE n.document_id IS UNIQUE
    """,
    """
    CREATE CONSTRAINT application_id IF NOT EXISTS
    FOR (n:Application) REQUIRE n.application_id IS UNIQUE
    """
]


# --------------------------------------------------
# 3. Helper functions
# --------------------------------------------------

def make_id(value):
    value = str(value).strip().lower()
    value = re.sub(r"[^a-z0-9]+", "_", value)
    return value.strip("_")


def create_child_nodes(tx, scheme_id, label, id_field,
                       relationship, values, language):
    query = f"""
    UNWIND $items AS item
    MATCH (s:Scheme {{scheme_id: $scheme_id}})
    MERGE (n:{label} {{{id_field}: item.id}})
    SET n.description = item.description,
        n.language = item.language
    MERGE (s)-[:{relationship}]->(n)
    """

    items = [
        {
            "id": f"{scheme_id}_{make_id(label)}_{language}_{i}",
            "description": str(value).strip(),
            "language": language
        }
        for i, value in enumerate(values, start=1)
        if value and str(value).strip()
    ]

    if items:
        tx.run(query, scheme_id=scheme_id, items=items)


# --------------------------------------------------
# 4. Import one scheme
# --------------------------------------------------

def import_scheme(tx, scheme):

    scheme_id = scheme.get("scheme_id")
    scheme_name = scheme.get("scheme_name_en")

    if not scheme_id or not scheme_name:
        raise ValueError("Scheme record is missing scheme_id or scheme_name_en")

    department_name = (
        scheme.get("department") or "Tamil Nadu Government"
    )

    department_id = make_id(department_name)

    source_id = (
        scheme.get("source_document")
        or scheme_id
    )

    # Department node
    tx.run(
        """
        MERGE (d:Department {department_id: $department_id})
        SET d.name = $department_name
        """,
        department_id=department_id,
        department_name=department_name
    )

    # Scheme node and Department relationship
    tx.run(
        """
        MATCH (d:Department {department_id: $department_id})
        MERGE (s:Scheme {scheme_id: $scheme_id})
        SET s.scheme_name_en = $name_en,
            s.scheme_name_ta = $name_ta,
            s.description_en = $description_en,
            s.description_ta = $description_ta,
            s.subsidy_details = $subsidy_details,
            s.official_url = $official_url,
            s.source_document = $source_document,
            s.source_page = $source_page,
            s.last_verified = $last_verified,
            s.verification_status = $verification_status
        MERGE (d)-[:OFFERS]->(s)
        """,
        department_id=department_id,
        scheme_id=scheme_id,
        name_en=scheme_name,
        name_ta=scheme.get("scheme_name_ta", ""),
        description_en=scheme.get("description_en", ""),
        description_ta=scheme.get("description_ta", ""),
        subsidy_details=scheme.get("subsidy_details", ""),
        official_url=scheme.get("official_url", ""),
        source_document=scheme.get("source_document", ""),
        source_page=scheme.get("source_page"),
        last_verified=scheme.get("last_verified", ""),
        verification_status=scheme.get("verification_status", "pending")
    )

    # Source node and relationship
    tx.run(
        """
        MATCH (s:Scheme {scheme_id: $scheme_id})
        MERGE (src:Source {source_id: $source_id})
        SET src.url = $url,
            src.document_name = $document_name
        MERGE (s)-[:VERIFIED_FROM]->(src)
        """,
        scheme_id=scheme_id,
        source_id=source_id,
        url=scheme.get("official_url", ""),
        document_name=scheme.get("source_document", "")
    )

    # Eligibility nodes
    create_child_nodes(
        tx, scheme_id, "Eligibility", "eligibility_id",
        "HAS_ELIGIBILITY",
        scheme.get("eligibility_en", []), "en"
    )
    create_child_nodes(
        tx, scheme_id, "Eligibility", "eligibility_id",
        "HAS_ELIGIBILITY",
        scheme.get("eligibility_ta", []), "ta"
    )

    # Benefit nodes
    create_child_nodes(
        tx, scheme_id, "Benefit", "benefit_id",
        "PROVIDES",
        scheme.get("benefits_en", []), "en"
    )
    create_child_nodes(
        tx, scheme_id, "Benefit", "benefit_id",
        "PROVIDES",
        scheme.get("benefits_ta", []), "ta"
    )

    # Required document nodes
    create_child_nodes(
        tx, scheme_id, "Document", "document_id",
        "REQUIRES",
        scheme.get("required_documents_en", []), "en"
    )
    create_child_nodes(
        tx, scheme_id, "Document", "document_id",
        "REQUIRES",
        scheme.get("required_documents_ta", []), "ta"
    )

    # Application process nodes
    create_child_nodes(
        tx, scheme_id, "Application", "application_id",
        "HAS_PROCESS",
        [scheme.get("application_process_en", "")], "en"
    )
    create_child_nodes(
        tx, scheme_id, "Application", "application_id",
        "HAS_PROCESS",
        [scheme.get("application_process_ta", "")], "ta"
    )


# --------------------------------------------------
# 5. Main execution
# --------------------------------------------------

def main():

    if not all([NEO4J_URI, NEO4J_USERNAME, NEO4J_PASSWORD]):
        raise ValueError(
            "Neo4j configuration missing. Check your .env file."
        )

    if not DATA_FILE.exists():
        raise FileNotFoundError(f"Scheme file not found: {DATA_FILE}")

    with open(DATA_FILE, "r", encoding="utf-8") as file:
        schemes = json.load(file)

    if not isinstance(schemes, list) or not schemes:
        raise ValueError("schemes.json is empty or has an invalid format.")

    print(f"Found {len(schemes)} scheme records.")
    print("Connecting to Neo4j AuraDB...")

    driver = GraphDatabase.driver(
        NEO4J_URI,
        auth=(NEO4J_USERNAME, NEO4J_PASSWORD)
    )

    try:
        driver.verify_connectivity()
        print("Neo4j connection successful!")

        with driver.session(database=NEO4J_DATABASE) as session:

            print("Creating uniqueness constraints...")

            for constraint in CONSTRAINTS:
                session.run(constraint).consume()

            print("Importing schemes...")

            successful = 0

            for scheme in schemes:
                session.execute_write(import_scheme, scheme)
                successful += 1
                print(
                    f"[{successful}/{len(schemes)}] "
                    f"Imported: {scheme.get('scheme_name_en')}"
                )

            print("\nImport completed successfully!")
            print(f"Total imported: {successful}")

    finally:
        driver.close()
        print("Neo4j driver closed.")


if __name__ == "__main__":
    main()
