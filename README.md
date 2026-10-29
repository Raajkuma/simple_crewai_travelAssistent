# CrewAI Travel Planner

An AI-powered travel recommendation script built with **CrewAI** and **Google Gemini**. Given a destination city, this tool uses an autonomous AI agent to generate a curated list of top places to visit along with concise descriptions and practical travel tips.

---

## Features

- **Automated Travel Agent**: Uses CrewAI's `Agent` and `Task` structures to query LLMs for realistic travel advice.
- **Gemini LLM Integration**: Powered by Google's `gemini-flash-latest` model for fast, accurate responses.
- **Structured Output**: Produces a clean list of exactly 3 recommended spots with tailored practical tips.

---

## Prerequisites

Before running this project, ensure you have the following installed:

- **Python**: Version 3.10 to 3.13 (CrewAI recommended range)
- **Google Gemini API Key**: An active API key from [Google AI Studio](https://aistudio.google.com/)

---

## Setup & Installation

### 1. Clone or Download the Project

Navigate to your working directory or place your script (e.g., `main.py`) in a dedicated folder.

### 2. Create a Virtual Environment (Recommended)

```bash
# On macOS/Linux
python3 -m venv venv
source venv/bin/activate

# On Windows (Command Prompt)
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

Install `crewai` and `python-dotenv`:

```bash
pip install crewai python-dotenv
```

### 4. Configure Environment Variables

Create a `.env` file in the root directory of your project:

```bash
touch .env
```

Add your Gemini API key to the `.env` file:

```env
GEMINI_API_KEY=your_google_gemini_api_key_here
```

---

## Usage

Run the main Python script:

```bash
python main.py
```

### Script Execution Flow:

1. **Input**: You will be prompted to enter a city name (e.g., `Paris`, `Tokyo`, or `New York`).
2. **Execution**: The CrewAI agent (`Travel Planner`) executes the task with verbose logging enabled.
3. **Output**: The script prints a structured travel itinerary with 3 places, brief descriptions, and actionable travel tips.

---

## Example Output

```text
Enter a city you want to visit: Tokyo

===== TRAVEL PLAN =====

1. Senso-ji Temple
   - Description: Tokyo's oldest and most significant Buddhist temple, located in Asakusa.
   - Travel Tip: Visit early in the morning or late in the evening to avoid heavy tourist crowds.

2. Shibuya Crossing & Hachiko Statue
   - Description: The world's busiest pedestrian intersection and a vibrant hub of youth culture and shopping.
   - Travel Tip: Head to the second-floor Starbucks in the Tsutaya building for a great elevated photo spot.

3. Meiji Shrine
   - Description: A peaceful Shinto shrine surrounded by a dense, tranquil forest in the middle of the city.
   - Travel Tip: Combine this visit with a stroll through neighboring Takeshita Street in Harajuku.
```

---

## Project Structure

```text
.
├── main.py           # Core script containing CrewAI setup and execution
├── .env              # Environment variables file containing API keys
└── README.md         # Project documentation
```
