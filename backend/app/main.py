from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from app.services.retrieval import RetrievalService
from app.services.generation import GenerationService
from app.api.routes.query import router as query_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    # تحميل الخدمات مرة واحدة عند الإقلاع
    app.state.retrieval_service = RetrievalService()
    app.state.generation_service = GenerationService()
    print("Vector store and Ollama client loaded successfully.")
    yield
    print("Application shutdown.")

app = FastAPI(
    title="Financial RAG Assistant API",
    version="1.0.0",
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "Financial RAG API"}

app.include_router(query_router)