
```markdown
# 🛤️ PathKeeper-Bot

**PathKeeper-Bot** is a daily AI-powered personal assistant designed for aspiring entrepreneurs. It delivers motivation, humor, spiritual reflection, and accountability via Telegram — tailored based on the time of day.

---

## 🔥 Features

- **Morning Motivation**: Gritty, no-nonsense pep talks to kickstart your day.
- **Noon Humor**: A smart dad/dark joke to lighten your mid-day mood.
- **Evening Reflection**: Personalized spiritual insights with prompts for gratitude, journaling, and planning.
- **Daily Japji Sahib Pauri**: A Sikh spiritual message from the Japji Sahib with Punjabi text, transliteration, translation, and simplified explanation.
- **Telegram Notification**: Sends all content directly to your Telegram chat.
- **Flexible Scheduling**: Can be triggered via AWS Lambda or local cron jobs.

---

## 📁 Project Structure



pathkeeper-bot/
├── agents.py
├── main.py
├── local\_execution.py
├── tasks.py
├── utils.py
├── .env
├── japji\_sahib\_full.json
├── requirements.txt
└── README.md

````

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/pathkeeper-bot.git
cd pathkeeper-bot
````

### 2. Create a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Create Your `.env` File

Create a `.env` file in the root directory with the following variables:

```env
GEMINI_API_KEY=your_gemini_api_key_here
TELEGRAM_BOT_TOKEN=your_telegram_bot_token_here
TELEGRAM_CHAT_ID=your_telegram_chat_id_here
DAILY_PAURI_INDEX=0
```

> 💡 To get your Telegram chat ID, you can use [@userinfobot](https://t.me/userinfobot) on Telegram.

---

## 🧠 How It Works

The bot chooses a task based on the current time:

| Time (24hr)   | Task Type                 |
| ------------- | ------------------------- |
| 05:00 - 11:59 | Morning Motivation        |
| 14:00 - 15:59 | Noon Humor                |
| 17:00 - 18:59 | Evening Japji Sahib Pauri |
| 22:00 - 23:00 | Night Reflection          |

Each task is powered by Google’s Gemini AI through the `CrewAI` framework and dispatched via Telegram.

---

## 🚀 Running the Bot

### Option 1: Run Locally (e.g., via `cron`)

```bash
python local_execution.py
```

Add this to your `crontab`:

```bash
0 10 * * * /Users/gurjyotanand/venv/bin/python /Users/gurjyotanand/Desktop/Projects_2025/Whatsapp_Message_AIBOT/local_execution.py
0 16 * * * /Users/gurjyotanand/venv/bin/python /Users/gurjyotanand/Desktop/Projects_2025/Whatsapp_Message_AIBOT/local_execution.py
0 20 * * * /Users/gurjyotanand/venv/bin/python /Users/gurjyotanand/Desktop/Projects_2025/Whatsapp_Message_AIBOT/local_execution.py
```

> 🔄 Make sure the path to your Python and script matches your system's directory structure.

### Option 2: Run via AWS Lambda

The `main.py` file is structured for AWS Lambda. Package the project and deploy:

```bash
zip -r pathkeeper-bot.zip .
# Then deploy using AWS Lambda console or CLI
```

Set a **CloudWatch Event Rule** to run `main.handler` at your desired times.

---

## 📘 JSON File: `japji_sahib_full.json`

This file contains all **41 pauris** from Japji Sahib with:

* `pauri_number`
* `pauri_punjabi`
* `transliteration`
* `translation`
* `explanation`

It is used for the evening spiritual message.

---

## 🧪 Testing

You can manually test by running:

```bash
python main.py
```

Or

```bash
python local_execution.py
```

---

## ✨ Future Enhancements

* Voice note delivery (TTS)
* Telegram reply integration for journaling
* Dashboard to visualize daily consistency
* Integration with Google Calendar or Notion

---

## 🙏 Credits

* Built using [CrewAI](https://github.com/joaomdmoura/crewAI)
* Powered by [Gemini AI](https://ai.google.dev/gemini-api/docs)
* Japji Sahib JSON manually curated for personalized daily reflections
* Telegram API for delivery

---

## 🧘‍♂️ Spiritual Note

> “Even one verse of Japji Sahib can redirect a distracted mind.”

Use this bot not just to stay productive, but also spiritually aligned.

---

## 🛠 Maintained by Gurjyot Anand

Cloud/DevOps Architect | Entrepreneur-in-Progress 🇮🇳➡️🇨🇦
Looking to automate inner and outer success, one script at a time.

---


