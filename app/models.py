from pydantic import BaseModel

class RecommendationRequest(BaseModel):
    interests: list[str]

class RecommendationResponse(BaseModel):
    recommended_place_ids: list[str]

class ChatbotRequest(BaseModel):
    user_input: str
