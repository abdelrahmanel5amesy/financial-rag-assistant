# 📊 Financial RAG Assistant (SEC 10-K Analysis)

An end-to-end Retrieval-Augmented Generation (RAG) assistant designed to analyze and compare SEC Form 10-K annual filings (FY2025) for Apple, Microsoft, and NVIDIA with strict contextual grounding and citation support.

---

## 🏗️ Architecture & Tech Stack

- Data Processing: pypdf, chunking strategy with fixed size (700 chars) and overlap (100 chars).
- Embeddings & Vector Store: sentence-transformers/all-MiniLM-L6-v2 with ChromaDB (persisted on disk).
- LLM: Local Ollama (llama3.2).
- Backend: FastAPI (serving /health and /query endpoints with startup lifespan initialization).
- Frontend: Streamlit chat interface with live citation expanding.

---

## 📁 Project Structure

rag-assistant-project/
├── backend/
│   ├── app/
│   │   ├── api/routes/query.py
│   │   ├── core/config.py
│   │   ├── schemas/query.py
│   │   ├── services/
│   │   │   ├── retrieval.py
│   │   │   └── generation.py
│   │   └── main.py
│   ├── tests/
│   │   └── test_query.py
│   ├── requirements.txt
│   └── .env.example
├── frontend/
│   ├── app.py
│   ├── api_client.py
│   ├── requirements.txt
│   └── .env
├── notebooks/
│   └── rag_pipeline.ipynb
├── data/
│   ├── rag_config.json
│   └── evaluation_results.csv
├── .gitignore
└── README.md

---

## ⚙️ Setup & Installation

### 1. Prerequisites
- Python 3.10+
- Ollama installed with llama3.2 pulled:
  ollama run llama3.2

### 2. Backend Setup
cd backend
pip install -r requirements.txt
cp .env.example .env
uvicorn app.main:app --reload

### 3. Frontend Setup
cd frontend
pip install -r requirements.txt
streamlit run app.py

---

## 📡 API Reference

### Health Check
curl -X GET http://localhost:8000/health

### Query Endpoint
curl -X POST http://localhost:8000/query -H "Content-Type: application/json" -d '{"question": "What was Apple total revenue in 2025?"}'

---

## 📈 Evaluation Results

Tested across 10 diverse financial benchmark queries. Company-based metadata routing prevented multi-company context collisions.

| Metric | Result |
|---|---|
| Retrieval Grounding | 100% adherence to provided context |
| Citation Accuracy | Complete document and page referencing |
| Average Latency | ~2-3s (Local inference) |