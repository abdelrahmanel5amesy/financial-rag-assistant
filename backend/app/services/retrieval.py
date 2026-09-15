import chromadb
from chromadb.utils import embedding_functions
from app.core.config import settings

class RetrievalService:
    def __init__(self):
        self.embedding_func = embedding_functions.SentenceTransformerEmbeddingFunction(
            model_name=settings.EMBEDDING_MODEL
        )
        self.client = chromadb.PersistentClient(path=settings.CHROMA_DB_PATH)
        self.collection = self.client.get_collection(
            name=settings.COLLECTION_NAME,
            embedding_function=self.embedding_func
        )

    def retrieve(self, query: str, top_k: int = 6):
        query_lower = query.lower()
        where_filter = None

        if "nvidia" in query_lower:
            where_filter = {"source": "Nvidia_annual2025.pdf"}
        elif "apple" in query_lower:
            where_filter = {"source": "Apple_annual2025.pdf"}
        elif "microsoft" in query_lower:
            where_filter = {"source": "Microsoft_annual2025.pdf"}

        query_args = {"query_texts": [query], "n_results": top_k}
        if where_filter:
            query_args["where"] = where_filter

        results = self.collection.query(**query_args)
        
        retrieved_texts = results["documents"][0]
        metadatas = results["metadatas"][0]

        context_blocks = []
        sources = set()

        for doc, meta in zip(retrieved_texts, metadatas):
            src_str = f"{meta['source']} (Page {meta['page']})"
            sources.add(src_str)
            context_blocks.append(f"[{src_str}]: {doc}")

        return "\n\n".join(context_blocks), list(sources)