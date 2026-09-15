from pydantic import BaseModel, Field
from typing import List

class QueryRequest(BaseModel):
    question: str = Field(..., min_length=2, description="The financial inquiry question.")

class QueryResponse(BaseModel):
    answer: str
    sources: List[str]