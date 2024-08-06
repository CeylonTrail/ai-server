from fastapi import FastAPI
from app.api import chatbot, sync, recommendation

app = FastAPI()

app.include_router(chatbot.router, prefix="/chatbot")
app.include_router(sync.router, prefix="/sync")
app.include_router(recommendation.router, prefix="/recommendation")
