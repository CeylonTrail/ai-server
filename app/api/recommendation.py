from fastapi import APIRouter, HTTPException
from app.models import RecommendationRequest, RecommendationResponse
from app.services.pinecone_service import perform_similarity_search

router = APIRouter()

@router.post("/")
async def recommendations(request: RecommendationRequest):
    try:
        return RecommendationResponse(perform_similarity_search(request.interests))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
