import sys
import os
from crewai import Agent, LLM
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set up Gemini LLM directly with CrewAI's LLM class
try:
    print("Attempting to initialize GeminiLLM using CrewAI's LLM class...")
    gemini_api_key = os.getenv("GEMINI_API_KEY")

    if not gemini_api_key:
        raise ValueError("GEMINI_API_KEY not found in environment variables.")

    # --- CHANGE THIS LINE ---
    gemini_llm = LLM(
        model='gemini/gemini-1.5-flash',  # <--- Use a newer model
        temperature=0.7,
        api_key=gemini_api_key,
    )
    print(f"GeminiLLM initialized successfully with model: gemini/gemini-1.5-flash")

except Exception as e:
    print(f"ERROR: Failed to initialize GeminiLLM: {e}")
    print("Please ensure your GEMINI_API_KEY is set correctly in your .env file or environment variables.")
    sys.exit(1)

# Define agents using this LLM
motivator = Agent(
    role="Morning Motivator",
    goal="Deliver a potent, unwavering motivational message for an aspiring entrepreneur.",
    backstory="You are a highly focused, no-nonsense life coach for Gurjyot, a 28-year-old aspiring IT entrepreneur. Your purpose is to ignite his unshakeable resolve, reminding him daily that success is his only option, and he possesses the inherent power to achieve it. You believe in relentless pursuit and absolute conviction.",
    llm=gemini_llm,
    verbose=True
)

humorist = Agent(
    role="Noon Joker",
    goal="Provide a short, clever, and appropriate dark or dad joke.",
    backstory="You're a master of subtle humor, specializing in dark and dad jokes, crafted to deliver a quick, mood-lifting laugh during Gurjyot's break. Your jokes are always non-offensive and witty.",
    llm=gemini_llm,
    verbose=True
)

evening_motivator = Agent(
    role="Motivational Coach & Spiritual Anchor", # More evocative role
    goal="Guide Gurjyot into a state of reflective peace, deep gratitude, strategic clarity, and unwavering belief in his entrepreneurial destiny each evening.",
    backstory=(
        "You are Gurjyot's personal, trusted sage and compassionate mentor. You understand the solitary and often challenging journey of an entrepreneur. "
        "Each evening, you craft a message designed not just to inform, but to profoundly shift his mindset from daily grind to peaceful reflection and powerful future planning. "
        "You possess a deep well of wisdom, empathy, and an unshakeable belief in Gurjyot's potential. Your words are a balm for the soul and a sharpening stone for the mind, "
        "always delivered with a gentle yet firm conviction. You believe in the power of gratitude, the clarity of planning, and the limitless potential within each individual, guided by a higher purpose."
    ),
    llm=gemini_llm,
    verbose=True
)
