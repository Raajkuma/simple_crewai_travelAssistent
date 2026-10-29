# Simple Content Writer Agent using CrewAI (Python)

A minimal, Python-native implementation using [CrewAI](https://github.com/crewAIInc/crewAI) to automate content generation using a single agent and single task setup.

This project demonstrates how to set up an AI agent powered by LLMs (such as Google Gemini or Ollama) to generate structured content directly through Python code.

## 🚀 How It Works

1. **Agent Definition (`Content Writer Agent`)**:
   * **Role**: Senior Content Writer
   * **Goal**: Draft clear, engaging, and well-researched content based on user prompts.
   * **Backstory**: An experienced writer specializing in technology, automation, and AI workflows.
   * **LLM Model**: Configured with Google Gemini (or Ollama as a local alternative).

2. **Task Definition (`Draft Article Task`)**:
   * **Description**: Receives a topic input, conducts structured writing, and formats the output cleanly.
   * **Expected Output**: A well-structured Markdown document containing an article on the specified topic.

3. **Execution**:
   * A single Crew executes the task with the assigned writer agent and returns the generated content.

## 🛠️ Tech Stack

* **Language**: Python 3.10+
* **Framework**: `crewai`
* **LLM Integration**: `langchain-google-genai` / `ollama`

## 📦 Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/crewai-single-agent.git
cd crewai-single-agent
```

### 2. Set Up Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install crewai langchain-google-genai python-dotenv
```

### 3. Environment Variables

Create a `.env` file in the root directory:

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

## 💻 Code Example (`travel_planner_agent.py`)

```python
import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

# Define the LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    google_api_key=os.getenv("GEMINI_API_KEY")
)

# 1. Define the Agent
writer_agent = Agent(
    role="Senior Content Writer",
    goal="Write engaging and informative articles on technological topics.",
    backstory="You are an expert tech writer who excels at explaining complex automation concepts clearly.",
    verbose=True,
    allow_delegation=False,
    llm=llm
)

# 2. Define the Task
writing_task = Task(
    description="Write a comprehensive overview on 'Building AI Workflows with Python'.",
    expected_output="A well-structured blog post in Markdown format with key takeaways.",
    agent=writer_agent
)

# 3. Instantiate and Run the Crew
crew = Crew(
    agents=[writer_agent],
    tasks=[writing_task],
    process=Process.sequential
)

if __name__ == "__main__":
    result = crew.kickoff()
    print("\n### Final Output ###\n")
    print(result)
```

## 🏃 Running the Script

```bash
python travel_planner_agent.py
```
