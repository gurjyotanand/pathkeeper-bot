from crewai import Crew
from tasks import morning_task, noon_task, night_task
from utils import send_telegram_message
from datetime import datetime
import json
import os
from dotenv import load_dotenv

load_dotenv()

def select_task():
    hour = datetime.now().hour
    if 8 <= hour < 11:
        return "morning", morning_task
    elif 14 <= hour < 16:
        return "noon", noon_task
    elif 17 <= hour <19:
        return "evening", None
    elif 2 <= hour <= 22:
        return "night", night_task
    else:
        return None, None

def get_current_pauri():
    JSON_PATH = "japji_sahib_full.json"
    ENV_PATH = ".env"
    TOTAL_PAURIS = 41  # Update based on actual pauri count

    with open(JSON_PATH, "r", encoding="utf-8") as f:
        pauris = json.load(f)

    current_index = int(os.getenv("DAILY_PAURI_INDEX", 0))
    pauri = pauris[current_index]

    text = f"""
🌙 **Pauri {pauri['pauri_number']} – Japji Sahib Reflection**

📜 **Punjabi**:
{pauri['pauri_punjabi']}

🔤 **Transliteration**:
{pauri['transliteration']}

🌍 **Translation**:
{pauri['translation']}

🧘 **Simple Explanation**:
{pauri['explanation']}
    """.strip()

    # Update the index for tomorrow
    next_index = (current_index + 1) % TOTAL_PAURIS
    _update_env_variable("DAILY_PAURI_INDEX", str(next_index), ENV_PATH)

    return text

def _update_env_variable(key, value, env_path):
    with open(env_path, "r") as f:
        lines = f.readlines()

    found = False
    for i, line in enumerate(lines):
        if line.startswith(f"{key}="):
            lines[i] = f"{key}={value}\n"
            found = True
            break
    if not found:
        lines.append(f"{key}={value}\n")

    with open(env_path, "w") as f:
        f.writelines(lines)

def run_ai_agent():
    label, task = select_task()
    if label:
        print(f"Running task for: {label}")

        if label == "evening":
            message = get_current_pauri()
            print("Generated Message:\n", message)
            send_telegram_message(message)
            return

        # Default agent task for morning/noon/night
        crew = Crew(
            agents=[task.agent],
            tasks=[task],
            verbose=True
        )
        result_object = crew.kickoff()
        generated_message = result_object.raw
        print("Generated Message:\n", generated_message)
        send_telegram_message(generated_message)
    else:
        print("Nothing to do at this hour.")

if __name__ == "__main__":
    run_ai_agent()
