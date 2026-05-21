from dotenv import load_dotenv # used to call key
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_agent
from datetime import datetime

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

def getdate():
    """Get the current datec
    """
    return datetime.now().strftime("%Y-%m-%d")

llm = ChatGoogleGenerativeAI(model="gemini-3-flash-preview")

system_prompt = """You are a helpful AI assistant. Answer clearly, concisely, and accurately.
"""

agent = create_agent(model=llm,  tools=[getdate], system_prompt=system_prompt)

user_query = input("enter your input: ")

response = agent.invoke({"messages":[{"role":"user", "content":user_query}]})
print(response["messages"][-1].content[0] ["text"])




