import requests
import os
from dotenv import load_dotenv

load_dotenv()

def post_to_channel(job):
    message = f"💼 *{job['title']}*\n🏢 {job['company']}\n🔗 [Apply here]({job['link']})"
    payload = {
        "chat_id": os.getenv("CHANNEL_USERNAME"),
        "text": message,
        "parse_mode": "Markdown"
    }
    url = f"https://api.telegram.org/bot{os.getenv('BOT_TOKEN')}/sendMessage"
    requests.post(url, data=payload)
