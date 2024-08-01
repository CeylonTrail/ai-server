from pydantic import BaseModel

class ChatbotRequest(BaseModel):
    user_input: str
