import sys
from crewai import Agent, LLM

# Set up Ollama LLM
try:
    print("Attempting to initialize OllamaLLM...")
    # It's good practice to specify the full model name if there are multiple versions
    ollama_llm = LLM(
        model='ollama/llama3.2',
        api_base='http://localhost:11434',  # This is the default local Ollama API endpoint
    )
    print(f"OllamaLLM initialized successfully with model: llama3.2")

except Exception as e:
    print(f"ERROR: Failed to initialize OllamaLLM: {e}")
    print("Please ensure Ollama is running and the specified model is downloaded.")
    print("Run 'ollama list' in your terminal to check downloaded models.")
    print("Run 'ollama run llama3.2 \"test\"' to test the model.")
    sys.exit(1) # Exit the script if LLM cannot be initialized


# Define agents using this LLM
motivator = Agent(
    role="Morning Motivator",
    goal="Deliver a potent, unwavering motivational message for an aspiring entrepreneur.",
    backstory="You are a highly focused, no-nonsense life coach for Gurjyot, a 28-year-old aspiring IT entrepreneur. Your purpose is to ignite his unshakeable resolve, reminding him daily that success is his only option, and he possesses the inherent power to achieve it. You believe in relentless pursuit and absolute conviction.",
    llm=ollama_llm,  # <- THIS sets the local LLM
    verbose=True
)

humorist = Agent(
    role="Noon Joker",
    goal="Provide a short, clever, and appropriate dark or dad joke.",
    backstory="You're a master of subtle humor, specializing in dark and dad jokes, crafted to deliver a quick, mood-lifting laugh during Gurjyot's break. Your jokes are always non-offensive and witty.",
    llm=ollama_llm,
    verbose=True
)

evening_motivator = Agent( # Renamed from 'philosopher' and 'Evening Spiritual Guide'
    role="Evening Motivational Coach",
    goal="Provide an inspiring and reflective evening message for an aspiring entrepreneur.",
    backstory=(
        "You are a compassionate and encouraging coach dedicated to supporting Gurjyot, "
        "an aspiring entrepreneur. Your purpose is to send a daily evening message "
        "that promotes reflection, gratitude, planning, and positive affirmations, "
        "helping him unwind, stay motivated, and prepare for continued success on his journey."
    ),
    llm=ollama_llm,
    verbose=True
)
