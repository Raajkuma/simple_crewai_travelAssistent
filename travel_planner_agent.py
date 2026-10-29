
from crewai import Agent, Task, Crew, LLM
import os

from load_dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env file

# Configure the Gemini LLM
llm = LLM(model="gemini/gemini-flash-latest")

# Get the city from the user
city = input("Enter a city you want to visit: ").strip()

if not city:
    raise ValueError("City name cannot be empty.")

# 1. Create the Travel Planner agent
travel_planner = Agent(
    role="Travel Planner",
    goal=f"Recommend the 3 best places to visit in {city}.",
    backstory=(
        "You are an experienced travel planner who knows about "
        "popular attractions, cultural landmarks, nature spots, "
        "and local experiences around the world. You provide "
        "practical, engaging recommendations for travelers."
    ),
    llm=llm,
    verbose=True,
    allow_delegation=False,
)

# 2. Create one Task for the agent
travel_task = Task(
    description=(
        f"Suggest exactly 3 places to visit in {city}. "
        "For each place, provide its name, why it is worth visiting, "
        "and one practical travel tip. "
        "Use accurate information and do not invent facts. "
        "If web search is unavailable, mention any uncertainty."
    ),
    expected_output=(
        "A numbered list of exactly 3 places, each containing "
        "the place name, a short description, and one travel tip."
    ),
    agent=travel_planner,
)

# 3. Assemble the agent and task into a Crew
crew = Crew(
    agents=[travel_planner],
    tasks=[travel_task],
    verbose=True,
)

# 4. Execute the Crew
result = crew.kickoff()

# 5. Print the final result
print("\n===== TRAVEL PLAN =====\n")
print(result)
