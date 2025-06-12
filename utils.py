# /utils.py
import datetime
import os
from dotenv import load_dotenv
import sys
import requests # Import the requests library for making HTTP requests

load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def send_telegram_message(msg): # Function name remains consistent, but functionality changes
    # Convert the CrewOutput object to a string to extract the message content
    message_content = str(msg)

    print(f"Attempting to send Telegram notification...", flush=True)

    if not TELEGRAM_BOT_TOKEN or not TELEGRAM_CHAT_ID:
        print("Error: TELEGRAM_BOT_TOKEN or TELEGRAM_CHAT_ID environment variables not set.", file=sys.stderr)
        print("Please set your Telegram bot token and chat ID in your .env file.", file=sys.stderr)
        print(f"Reminder: {message_content}", flush=True) # Fallback to console print
        return

    telegram_api_url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message_content
    }

    try:
        response = requests.post(telegram_api_url, data=payload)
        response.raise_for_status() # Raise an HTTPError for bad responses (4xx or 5xx)
        print("Telegram notification sent successfully!", flush=True)
    except requests.exceptions.RequestException as e:
        print(f"Failed to send Telegram notification: {e}", file=sys.stderr)
        print(f"Please check your network connection, Telegram bot token, and chat ID.", file=sys.stderr)
        print(f"Falling back to console message.", file=sys.stderr)
        print(f"Reminder: {message_content}", flush=True) # Fallback to console print
    except Exception as e:
        print(f"An unexpected error occurred while sending Telegram notification: {e}", file=sys.stderr)
        print(f"Falling back to console message.", file=sys.stderr)
        print(f"Reminder: {message_content}", flush=True) # Fallback to console print

