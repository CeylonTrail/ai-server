from fastapi import APIRouter, HTTPException
from app.models import ChatbotRequest
from app.services.chatbot_service import process_chatbot_input

router = APIRouter()

@router.post("/")
async def chatbot_response(request: ChatbotRequest):
    try:
        response = process_chatbot_input(request.user_input)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
