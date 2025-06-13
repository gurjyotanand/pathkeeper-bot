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
        "**Craft a personalized, deeply inspiring, and reflective evening message for an aspiring entrepreneur, Gurjyot.** "
        "The message should feel like a direct, empathetic conversation from a seasoned mentor, designed to help Gurjyot unwind, reflect, and prepare for tomorrow's challenges with renewed vigor. "
        "The flow should be organic, not like a checklist, weaving together these elements seamlessly:\n\n"
        "1.  **Personal Check-in:** Begin with a warm, genuine inquiry about Gurjyot's day, specifically focusing on productivity and progress, acknowledging both wins and challenges without dwelling on negatives.\n"
        "2.  **Guided Gratitude:** Transition smoothly into a specific, thought-provoking prompt for gratitude that encourages deep reflection on what went well or positive lessons learned today. Avoid generic 'three things' lists; inspire a singular, impactful reflection.\n"
        "3.  **Actionable Journaling & Planning:** Encourage journaling not just about the day, but explicitly link it to strategic planning for tomorrow. Emphasize that journaling is a tool for clarity and execution, not just reflection. Guide him to identify ONE pivotal action for tomorrow.\n"
        "4.  **Powerful Affirmation & Future Vision:** Provide a potent, concise affirmation that reinforces his entrepreneurial path and future success. This should feel like a direct declaration of his potential, inspiring confidence and wealth attraction.\n"
        "5.  **Unique Uplifting Quote:** Integrate a short, impactful, and less common motivational quote that resonates with themes of perseverance, vision, or inner strength. Ensure it's fresh each time.\n"
        "6.  **Heartfelt Spiritual Acknowledgment:** Conclude with a brief, sincere expression of thanks to a higher power/God for guidance and opportunity, fostering a sense of peace and divine support.\n\n"
        "**Crucially, the tone must be:** Supportive, profound, direct, and deeply personal. Avoid bullet points, numbered lists, or overly formal language. Make it feel like a single, flowing message. Do NOT use phrases like 'three things' or 'grab your journal'. Instead, weave these actions into natural language."
    ),
    agent=evening_motivator,
    expected_output=(
        "A cohesive, personalized, and highly motivational evening message for Gurjyot, flowing naturally from a check-in to gratitude, strategic planning, a powerful affirmation, a unique uplifting quote, and a spiritual acknowledgment. The tone must be that of a direct, empathetic, and wise mentor, inspiring peace and continued drive. The message should be a single block of text, without bullet points or numbered lists."
    )
)
