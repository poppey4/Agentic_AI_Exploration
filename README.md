Agentic_AI_Exploration/
│
├── app/
│   ├── agents/
│   │   ├── ingestion_agent.py
│   │   ├── retrieval_agent.py
│   │   ├── sql_agent.py
│   │   ├── quality_agent.py
│   │   └── governance_agent.py
│   │
│   ├── rag/
│   │   ├── embeddings.py
│   │   ├── vector_store.py
│   │   └── retriever.py
│   │
│   ├── workflows/
│   │   └── temporal_workflow.py
│   │
│   ├── api/
│   │   └── main.py
│   │
│   ├── ui/
│   │   └── streamlit_app.py
│   │
│   └── utils/
│       └── helper.py
│
├── data/
├── notebooks/
├── tests/
├── screenshots/
├── requirements.txt
├── README.md
├── Dockerfile
├── .gitignore
└── docker-compose.yml

# AgentFlow AI
Enterprise-grade Multi-Agent AI Platform combining:

- LangChain
- RAG Pipelines
- Databricks
- PySpark
- Temporal
- ChromaDB
- FastAPI
- Streamlit
- Azure-ready architecture
## Features

### Multi-Agent Architecture
- Ingestion Agent
- Retrieval Agent
- SQL Generation Agent
- Data Quality Agent
- Governance Agent

### Enterprise AI Capabilities
- Document Intelligence
- Retrieval-Augmented Generation (RAG)
- Semantic Search
- Natural Language to SQL
- AI-powered Data Quality Validation
- Metadata & Governance Simulation

## Tech Stack

| Layer | Technology |
|---|---|
| LLM Framework | LangChain |
| Data Processing | PySpark |
| Vector DB | ChromaDB |
| Frontend | Streamlit |
| Backend | FastAPI |
| Orchestration | Temporal |
| Cloud | Azure / Databricks |
| Storage | Delta Lake |

## Run Locally

```bash
pip install -r requirements.txt
streamlit run app/ui/streamlit_app.py
