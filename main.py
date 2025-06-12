import os
import json
from datetime import datetime
from zoneinfo import ZoneInfo


import random # Import the random module

# Import crewai components
from crewai import Crew, Agent, Task # Assuming Agent and Task are used

# Import your local modules
from tasks import morning_task, noon_task, night_task
from utils import send_telegram_message

# --- Constants ---
JSON_PATH = "japji_sahib_full.json" # This file must be in your deployment package root

# --- Helper Functions ---

def select_task():
    # Use Toronto timezone regardless of where this runs
    hour = datetime.now(ZoneInfo("America/Toronto")).hour
    if 5 <= hour < 12:
        return "morning", morning_task
    elif 14 <= hour < 16:
        return "noon", noon_task
    elif 18 <= hour < 20:
        return "evening", None
    elif 22 <= hour <= 23:
        return "night", night_task
    else:
        return None, None


def get_random_pauri():
    """Retrieves a random pauri from the JSON file."""
    try:
        with open(JSON_PATH, "r", encoding="utf-8") as f:
            pauris = json.load(f)
    except FileNotFoundError:
        print(f"Error: {JSON_PATH} not found in the deployment package.")
        send_telegram_message(f"Error: Japji Sahib JSON file not found in Lambda. Please check deployment.")
        raise

    # Select a random pauri
    random_pauri = random.choice(pauris)

    text = f"""
🌙 **Pauri {random_pauri['pauri_number']} – Japji Sahib Reflection**

📜 **Punjabi**:
{random_pauri['pauri_punjabi']}

🔤 **Transliteration**:
{random_pauri['transliteration']}

🌍 **Translation**:
{random_pauri['translation']}

🧘 **Simple Explanation**:
{random_pauri['explanation']}
    """.strip()

    return text

def run_ai_agent():
    label, task_obj = select_task()
    if label:
        print(f"Running task for: {label}")

        if label == "evening":
            # Evening task now gets a random pauri
            message = get_random_pauri()
            print("Generated Message:\n", message)
            send_telegram_message(message)
            return

        # Default agent task for morning/noon/night
        if task_obj and hasattr(task_obj, 'agent'):
            crew = Crew(
                agents=[task_obj.agent],
                tasks=[task_obj],
                verbose=True
            )
            result_object = crew.kickoff()
            generated_message = result_object.raw
            print("Generated Message:\n", generated_message)
            send_telegram_message(generated_message)
        else:
            print(f"No valid agent or task found for {label}. Skipping AI agent run.")

    else:
        print("Nothing to do at this hour.")

# --- AWS Lambda Handler ---
def handler(event, context):
    """
    The main entry point for the AWS Lambda function.
    """
    print("Lambda function invoked!")
    run_ai_agent()

    return {
        'statusCode': 200,
        'body': json.dumps('Bot execution completed successfully!')
    }

# This part is only for local testing, won't run in Lambda
if __name__ == "__main__":
    print("Running locally (not in Lambda)...")
    run_ai_agent()
