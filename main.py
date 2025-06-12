from crewai import Crew
from tasks import morning_task, noon_task, night_task
from utils import send_telegram_message
from datetime import datetime


def select_task():
    hour = datetime.now().hour

    if 1 <= hour < 10:
        return "morning", morning_task
    elif 14 <= hour < 16:
        return "noon", noon_task
    elif 20 <= hour <= 22:
        return "night", night_task
    else:
        return None, None

def run_ai_agent():
    label, task = select_task()
    if task:
        print(f"Running task for: {label}")
        crew = Crew(
            agents=[task.agent],
            tasks=[task],
            verbose=True
        )
        result_object = crew.kickoff() # Renamed to avoid confusion with the string 'result'
        
        # Access the raw string output from the CrewOutput object
        generated_message = result_object.raw 
        
        print("Generated Message:\n", generated_message)
        send_telegram_message(generated_message)
    else:
        print("Nothing to do at this hour.")

if __name__ == "__main__":
    run_ai_agent()
