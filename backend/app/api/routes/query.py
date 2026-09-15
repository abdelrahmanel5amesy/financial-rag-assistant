from fastapi import APIRouter, Request, HTTPException
from app.schemas.query import QueryRequest, QueryResponse

router = APIRouter()

@router.post("/query", response_model=QueryResponse)
async def query_assistant(request: Request, body: QueryRequest):
    retrieval_service = request.app.state.retrieval_service
    generation_service = request.app.state.generation_service

    try:
        context, sources = retrieval_service.retrieve(body.question)
        answer = generation_service.generate_answer(body.question, context)
        return QueryResponse(answer=answer, sources=sources)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))