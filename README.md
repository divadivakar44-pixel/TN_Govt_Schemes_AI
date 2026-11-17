# Tamil Nadu Government Schemes AI Assistant

An AI-powered bilingual (English and Tamil) assistant that helps users discover and understand Tamil Nadu Government schemes related to Agriculture, Farmers Welfare, Horticulture and Micro, Small and Medium Enterprises (MSME).

The application uses Knowledge Graph Retrieval-Augmented Generation (GraphRAG) to retrieve scheme-related information from government documents and generate contextual answers using an OpenAI language model.

## 1. Project Overview

Finding relevant government schemes, understanding eligibility criteria, identifying available subsidies and following application procedures can be challenging.

This project addresses that challenge by providing a conversational AI assistant that allows users to ask questions in English or Tamil and receive answers based on structured government scheme information.

### Key Objectives

- Centralize Tamil Nadu Government scheme information.
- Provide bilingual scheme-related assistance.
- Retrieve relevant information through a Neo4j Knowledge Graph.
- Generate contextual responses using LangChain and OpenAI.
- Provide a simple interactive interface using Streamlit.
- Validate user queries using NVIDIA NeMo Guardrails.
- Expose backend services through FastAPI.

## 2. Key Features

- **Bilingual Assistance:** Supports English and Tamil questions.
- **Knowledge Graph:** Stores schemes, departments, eligibility criteria, benefits and source information in Neo4j.
- **GraphRAG Integration:** Retrieves relevant scheme information before generating answers.
- **AI-powered Responses:** Uses OpenAI through LangChain.
- **Guardrails:** Restricts unrelated questions and helps keep the assistant within its intended domain.
- **FastAPI Backend:** Provides API endpoints for application communication.
- **Streamlit Frontend:** Provides an interactive chat interface.
- **Source Traceability:** Maintains source document references and scheme verification status.

## 3. Technology Stack

| Component | Technology |
|---|---|
| Programming Language | Python |
| Knowledge Graph Database | Neo4j AuraDB |
| LLM | OpenAI |
| LLM Framework | LangChain |
| Retrieval Architecture | GraphRAG |
| Backend | FastAPI |
| Frontend | Streamlit |
| AI Guardrails | NVIDIA NeMo Guardrails |
| Data Processing | Pandas, BeautifulSoup, PyPDF |
| API Communication | REST API |
| Configuration Management | Python-dotenv |

## 4. System Architecture

```text
Government Scheme Documents
           |
           v
   Data Collection
           |
           v
   Document Extraction
           |
           v
   Data Processing
           |
           v
   Structured Scheme Data
           |
           v
    Neo4j AuraDB
   Knowledge Graph
           |
           v
   LangChain GraphRAG
           |
           v
       OpenAI LLM
           |
           v
   NVIDIA NeMo Guardrails
           |
           v
      FastAPI Backend
           |
           v
     Streamlit Frontend
           |
           v
       User Response
```

## 5. Knowledge Graph Design

The Neo4j Knowledge Graph contains the following node types:

- Department
- Scheme
- Eligibility
- Benefit
- Document
- Application
- Source

### Relationships

| Relationship | Description |
|---|---|
| OFFERS | Department offers a scheme |
| HAS_ELIGIBILITY | Scheme has eligibility conditions |
| PROVIDES | Scheme provides benefits |
| REQUIRES | Scheme requires documents |
| HAS_PROCESS | Scheme has an application process |
| VERIFIED_FROM | Scheme is associated with a source document |

This graph structure enables the application to retrieve connected scheme information rather than relying only on unstructured text.

## 6. Project Structure

```text
TN_Govt_Schemes_AI/
│
├── backend/
│   └── main.py
│
├── frontend/
│   └── app.py
│
├── knowledge_graph/
│   ├── graph_retriever.py
│   ├── langchain_pipeline.py
│   ├── load_schemes_to_neo4j.py
│   └── test_retriever.py
│
├── guardrails/
│   ├── config.yml
│   ├── rails.co
│   └── actions.py
│
├── data/
│   ├── raw/
│   ├── processed/
│   │   ├── extracted_documents.json
│   │   └── schemes.json
│   └── sources.json
│
├── collect_sources.py
├── extract_documents.py
├── identify_scheme_candidates.py
├── list_scheme_headings.py
├── populate_msme_schemes.py
│
├── test_neo4j.py
├── test_openai.py
├── test_guardrails.py
│
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

## 7. Prerequisites

Install the following before running the application:

- Python 3.11
- Git
- Neo4j AuraDB account and database
- OpenAI API key

## 8. Installation and Setup

### Step 1: Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/TN_Govt_Schemes_AI.git
cd TN_Govt_Schemes_AI
```

### Step 2: Create a Virtual Environment

```bash
py -3.11 -m venv venv
```

Activate the environment on Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, use the virtual environment's Python executable directly.

### Step 3: Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### Step 4: Configure Environment Variables

Create a `.env` file in the project root directory.

Add the following configuration:

```env
OPENAI_API_KEY=your_openai_api_key
OPENAI_MODEL=gpt-4o-mini

NEO4J_URI=neo4j+s://your_instance_id.databases.neo4j.io
NEO4J_USERNAME=neo4j
NEO4J_PASSWORD=your_neo4j_password
NEO4J_DATABASE=neo4j
```

Replace the placeholder values with your own credentials.

**Security:** Never upload `.env` or expose API keys and database passwords in GitHub.

## 9. Database Setup

1. Create a Neo4j AuraDB instance.
2. Configure the database credentials in `.env`.
3. Test the connection:

```bash
python test_neo4j.py
```

4. Import structured scheme records:

```bash
python knowledge_graph/load_schemes_to_neo4j.py
```

The import script creates the required graph nodes, relationships and uniqueness constraints.

## 10. Running the Application

### Start FastAPI Backend

Open the first terminal:

```bash
python -m uvicorn backend.main:app --reload --host 127.0.0.1 --port 8000
```

API documentation:

http://127.0.0.1:8000/docs

Health endpoint:

http://127.0.0.1:8000/health

### Start Streamlit Frontend

Open a second terminal:

```bash
python -m streamlit run frontend/app.py
```

Access the application:

http://localhost:8501

Keep the FastAPI backend running while using Streamlit.

## 11. Example Questions

### English

- What subsidies are available for MSMEs?
- What is the eligibility for generator subsidy?
- Explain the PEACE energy audit scheme.
- What benefits are available under the Q-CERT scheme?

### Tamil

- சிறு தொழில்களுக்கு என்ன மானியங்கள் உள்ளன?
- ஜெனரேட்டர் மானியம் பெறுவதற்கான தகுதிகள் என்ன?
- ஆற்றல் தணிக்கை திட்டத்தின் நன்மைகள் என்ன?

Responses depend on the scheme records available in the Knowledge Graph.

## 12. Testing

The project includes test scripts for individual components.

| Test File | Purpose |
|
