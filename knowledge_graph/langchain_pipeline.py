
from langchain_core.documents import Document
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

from knowledge_graph.graph_retriever import SchemeGraphRetriever


class SchemeGraphRAG:

    def __init__(self):

        self.retriever = SchemeGraphRetriever()

        self.llm = ChatOpenAI(
            model="gpt-4o-mini",
            temperature=0
        )

        self.prompt = ChatPromptTemplate.from_messages([
            (
                "system",
                """
                You are a Tamil Nadu Government Schemes Assistant.

                Answer using only the retrieved government information.

                Rules:
                1. Do not invent scheme details.
                2. Do not invent eligibility or subsidy amounts.
                3. If information is unavailable, say so.
                4. Mention the official source when available.
                5. Answer in the language used by the user.
                """
            ),
            (
                "human",
                """
                User Question:
                {question}

                Retrieved Government Information:
                {context}
                """
            )
        ])

    def ask(self, question):

        records = self.retriever.retrieve(question)

        if not records:
            return {
                "answer": (
                    "The requested information is not available "
                    "in the retrieved government data."
                ),
                "sources": []
            }

        context = "\n".join(
            str(record) for record in records
        )

        chain = self.prompt | self.llm

        response = chain.invoke({
            "question": question,
            "context": context
        })

        sources = sorted({
            url
            for record in records
            for url in (record.get("sources") or [])
            if url
        })

        return {
            "answer": response.content,
            "sources": sources
        }

    def close(self):
        self.retriever.close()


if __name__ == "__main__":

    rag = SchemeGraphRAG()

    try:
        question = input("Ask your question: ")

        result = rag.ask(question)

        print("\nAI ANSWER:")
        print(result["answer"])

        print("\nOFFICIAL SOURCES:")
        for source in result["sources"]:
            print(source)

    finally:
        rag.close()
