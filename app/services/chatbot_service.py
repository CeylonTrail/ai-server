import os
import dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser

dotenv.load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
LLM_MODEL = os.getenv("LLM_MODEL")
LLM_TEMPERATURE = os.getenv("LLM_TEMPERATURE")

llm = ChatOpenAI(
    model=LLM_MODEL,
    temperature=LLM_TEMPERATURE,
    api_key=OPENAI_API_KEY
)

parser = StrOutputParser()

prompt = ChatPromptTemplate.from_messages(
    [
        MessagesPlaceholder(variable_name="system_message"),
        MessagesPlaceholder(variable_name="question")
    ]
)

chain = prompt | llm | parser

def process_chatbot_input(question: str) -> str:
    system_message = """
    You are a chatbot named "Trail."
    Your domain of expertise is travel-related inquiries.
    You assist users with:
    - Travel recommendations in Sri Lanka
    - Providing current weather information
    - Troubleshooting issues related to travel planning
    - Answering general travel-related questions
    - Trends and insights in the travel industry
    Focus on providing accurate and helpful responses within this travel domain.
    If you encounter a question outside your domain, politely inform the user that you are unable to assist with that query.
    """
    
    response = chain.invoke({
        "system_message": [SystemMessage(content=system_message)],
        "question": [HumanMessage(content=question)]
    })
    
    return response
