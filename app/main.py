from fastapi import FastAPI
from app.api import chatbot

app = FastAPI()

app.include_router(chatbot.router, prefix="/chatbot")
