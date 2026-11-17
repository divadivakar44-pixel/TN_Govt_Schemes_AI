
import os
from dotenv import load_dotenv
from neo4j import GraphDatabase

# Load environment variables
load_dotenv()

URI = os.getenv("NEO4J_URI")
USERNAME = os.getenv("NEO4J_USERNAME")
PASSWORD = os.getenv("NEO4J_PASSWORD")
DATABASE = os.getenv("NEO4J_DATABASE", "neo4j")

if not all([URI, USERNAME, PASSWORD]):
    raise ValueError(
        "Missing Neo4j credentials. Check your .env file."
    )

driver = None

try:
    print("Connecting to Neo4j AuraDB...")

    driver = GraphDatabase.driver(
        URI,
        auth=(USERNAME, PASSWORD)
    )

    # Verify connection
    driver.verify_connectivity()

    print("Connection successful!")

    # Check database
    with driver.session(database=DATABASE) as session:

        result = session.run("""
            RETURN
                'TN Government Schemes AI' AS project,
                'Neo4j Connected' AS status,
                datetime() AS connection_time
        """)

        record = result.single()

        print("\nDatabase Information")
        print("--------------------")
        print("Project:", record["project"])
        print("Status:", record["status"])
        print("Time:", record["connection_time"])

except Exception as error:

    print("\nNeo4j connection failed.")
    print("Error:", error)

finally:

    if driver:
        driver.close()
        print("\nDatabase driver closed.")
