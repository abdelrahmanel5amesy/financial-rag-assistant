import ollama
from app.core.config import settings

class GenerationService:
    def __init__(self):
        self.client = ollama.Client(host=settings.OLLAMA_HOST)
        self.model = settings.OLLAMA_MODEL

    def generate_answer(self, question: str, context: str) -> str:
        system_prompt = (
            "You are a financial analysis assistant. Answer the user's question strictly using the provided context.\n"
            "Always cite the source document and page number for facts and figures.\n"
            "If the information is not in the context, say you don't know based on the files."
        )

        user_content = f"Context:\n{context}\n\nQuestion: {question}\nAnswer:"

        response = self.client.chat(
            model=self.model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_content}
            ]
        )
        return response["message"]["content"]