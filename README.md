# Job Posting Bot

This project scrapes jobs from [RemoteOK](https://remoteok.com) and automatically posts them to your Telegram channel using a bot.

## Features

- Web scraping for fresh job posts
- Deduplication to avoid reposts
- Telegram bot posting
- Clean modular structure

## Setup

1. Clone the repo:

```bash
git clone https://github.com/yourusername/job-posting-bot.git
cd job-posting-bot
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Create a `.env` file:

```
BOT_TOKEN=your_telegram_bot_token
CHANNEL_USERNAME=@yourchannel
JOB_SOURCE_URL=https://remoteok.com/remote-dev-jobs
```

4. Run the bot:

```bash
python main.py
```

## Deploy

- Use `cron` or `APScheduler` to run the script daily/hourly.
