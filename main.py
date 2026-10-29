from crewai import Agent, Task,Crew, LLM

from load_dotenv import load_dotenv
import os
load_dotenv()  # Load environment variables from .env file

print(os.getenv("GEMINI_API_KEY"))  # Print the value of GEMINI_API_KEY

llm = LLM(model = "gemini/gemini-flash-latest")

print(llm)