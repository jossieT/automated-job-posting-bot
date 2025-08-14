import requests
import os
from dotenv import load_dotenv

load_dotenv()

def post_to_channel(job):
    message = f"\U0001F4BC *{job['title']}*\n\U0001F3E2 {job['company']}\n\U0001F517 [Apply here]({job['link']})"
    payload = {
        "chat_id": os.getenv("CHANNEL_USERNAME"),
        "text": message,
        "parse_mode": "Markdown"
    }
    url = f"https://api.telegram.org/bot{os.getenv('BOT_TOKEN')}/sendMessage"
    print(f"[INFO] Sending POST to Telegram: {url}")
    print(f"[DEBUG] Payload: {payload}")
    response = requests.post(url, data=payload)
    print(f"[INFO] Telegram response status: {response.status_code}")
    print(f"[DEBUG] Telegram response: {response.text}")
