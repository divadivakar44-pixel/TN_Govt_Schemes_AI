
from pathlib import Path
import sys
import traceback

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from dotenv import load_dotenv

# Project root
BASE_DIR = Path(__file__).resolve().parent.parent

# Load environment variables
load_dotenv(BASE_DIR / ".env")

# Allow imports from project root
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

app = FastAPI(
    title="Tamil Nadu Government Schemes AI",
    description=(
        "Bilingual AI assistant for Tamil Nadu "
        "Agriculture, Farmers Welfare and MSME schemes."
    ),
    version="1.0.0"
)

# Frontend connection
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ChatRequest(BaseModel):
    question: str = Field(
        ...,
        min_length=2,
        max_length=2000
    )


class ChatResponse(BaseModel):
    question: str
    answer: str
    sources: list[str] = []


@app.get("/")
def home():
    return {
        "message": "Tamil Nadu Government Schemes AI Backend",
        "status": "running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "project": "TN_Govt_Schemes_AI"
    }


@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):

    try:
        question = request.question.strip()

        if not question:
            raise HTTPException(
                status_code=400,
                detail="Please enter a valid question."
            )

        from knowledge_graph.langchain_pipeline import SchemeGraphRAG

        rag = SchemeGraphRAG()

        try:
            result = rag.ask(question)
        finally:
            rag.close()

        if isinstance(result, dict):
            answer = result.get("answer", "")
            sources = result.get("sources", [])
        else:
            answer = str(result)
            sources = []

        return ChatResponse(
            question=question,
            answer=answer,
            sources=sources
        )

    except HTTPException:
        raise

    except Exception as error:
        traceback.print_exc()

        raise HTTPException(
            status_code=500,
            detail=f"Unable to process question: {str(error)}"
        )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "backend.main:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )
