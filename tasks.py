from crewai import Task
from agents import motivator, humorist, evening_motivator

morning_task = Task(
    description=(
        "Write a bold and direct 2-3 line good morning message for an aspiring entrepreneur named Gurjyot. "
        "The tone must be no-nonsense, gritty, and real — as if it's coming from a battle-hardened coach. "
        "Use powerful short sentences. Address Gurjyot by name. Emphasize personal responsibility and action."
        "End the message with a famous motivational quote that aligns with the theme, such as but give new everytime:\n"
        "- 'No one's coming to save you. Get up. Be your own hero.'\n"
        "- 'Stop dreaming. Start doing.'\n"
        "- 'Discipline is the bridge between goals and accomplishment.' - Jim Rohn\n"
        "Avoid fluff. Speak with conviction. No apologies. No soft tone. Start the message with Good Morning Millionare."
    ),
    agent=motivator,
    expected_output="A short but intense morning motivation, addressing Gurjyot by name, ending with a powerful quote (real or attributed)."
)

noon_task = Task(
    description=(
        "Generate a 1-2 line joke. It must be either a dark joke or a dad joke, "
        "and absolutely non-offensive. The joke should be clever and designed "
        "to provide a quick moment of lightheartedness."
    ),
    agent=humorist,
    expected_output="A short, non-offensive dark joke or dad joke. Format: Joke of the day: <joke>"
)

night_task = Task(
    description=(
        "**Craft a personalized evening reflection message for an aspiring entrepreneur.** "
        "The message should cover the following points:\n\n"
        "1.  **Check-in:** Ask about their day, specifically if it was productive. (e.g., 'How was your day, Gurjyot? Was it productive?').\n"
        "2.  **Gratitude:** Include a prompt for gratitude, encouraging reflection on positive aspects. (e.g., 'Take a moment to reflect on what you're grateful for today.').\n"
        "3.  **Journaling Prompt:** Encourage journaling about the day's events and planning for tomorrow. (e.g., 'Before you sleep, journal about your day's experiences and outline your plans for tomorrow.').\n"
        "4.  **Affirmation of Success:** Offer a positive affirmation about future success/wealth. (e.g., 'Remember, you are on the path to becoming incredibly successful.').\n"
        "5.  **Positive Quote:** Include a short, uplifting quote that inspires a positive vibe.\n"
        "6.  **Spiritual Acknowledgment:** Conclude with a note of thanks to a higher power/God. (e.g., 'Thank God for all the blessings.').\n\n"
        "Keep it short. Ensure the tone is supportive, encouraging, and geared towards someone on an entrepreneurial journey, fostering a sense of peace and motivation before sleep."
    ),
    agent=evening_motivator, # Renamed the agent to fit the new role
    expected_output=(
        "A multi-point evening message including a daily check-in, gratitude prompt, "
        "journaling encouragement, a positive affirmation of future success, an uplifting quote, "
        "and a note of thanks to a higher power."
    )
)
