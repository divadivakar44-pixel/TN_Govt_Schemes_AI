
import os
from dotenv import load_dotenv
from neo4j import GraphDatabase

load_dotenv()

URI = os.getenv("NEO4J_URI")
USERNAME = os.getenv("NEO4J_USERNAME")
PASSWORD = os.getenv("NEO4J_PASSWORD")
DATABASE = os.getenv("NEO4J_DATABASE", "neo4j")


class SchemeGraphRetriever:

    def __init__(self):
        self.driver = GraphDatabase.driver(
            URI,
            auth=(USERNAME, PASSWORD)
        )

        self.driver.verify_connectivity()

    def retrieve(self, question):

        query = """
        MATCH (d:Department)-[:OFFERS]->(s:Scheme)

        OPTIONAL MATCH (s)-[:HAS_ELIGIBILITY]->(e:Eligibility)
        OPTIONAL MATCH (s)-[:PROVIDES]->(b:Benefit)
        OPTIONAL MATCH (s)-[:REQUIRES]->(doc:Document)
        OPTIONAL MATCH (s)-[:HAS_PROCESS]->(a:Application)
        OPTIONAL MATCH (s)-[:VERIFIED_FROM]->(src:Source)

        WITH d, s,
             collect(DISTINCT e.description) AS eligibility,
             collect(DISTINCT b.description) AS benefits,
             collect(DISTINCT doc.name) AS documents,
             collect(DISTINCT a.description) AS applications,
             collect(DISTINCT src.url) AS sources

        WHERE
            toLower(s.scheme_name_en) CONTAINS toLower($question)
            OR toLower(d.name) CONTAINS toLower($question)
            OR any(x IN eligibility
                WHERE toLower(coalesce(x, '')) CONTAINS toLower($question))
            OR any(x IN benefits
                WHERE toLower(coalesce(x, '')) CONTAINS toLower($question))
            OR toLower(s.description_en) CONTAINS toLower($question)

        RETURN
            d.name AS department,
            s.scheme_name_en AS scheme,
            s.description_en AS description,
            eligibility,
            benefits,
            documents,
            applications,
            sources

        LIMIT 10
        """

        with self.driver.session(database=DATABASE) as session:
            result = session.run(
                query,
                question=question
            )

            return [record.data() for record in result]

    def close(self):
        self.driver.close()


if __name__ == "__main__":

    retriever = SchemeGraphRetriever()

    try:
        question = input("Enter your scheme question: ")

        results = retriever.retrieve(question)

        if results:
            for index, result in enumerate(results, start=1):
                print(f"\nScheme {index}")
                print(result)
        else:
            print("No matching scheme found in the knowledge graph.")

    finally:
        retriever.close()
