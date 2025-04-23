from job_scraper.scraper import scrape_jobs
from telegram_poster.poster import post_to_channel
from utils.deduplicator import is_duplicate, save_posted

def main():
    jobs = scrape_jobs()
    for job in jobs:
        if not is_duplicate(job['link']):
            post_to_channel(job)
            save_posted(job['link'])

if __name__ == "__main__":
    main()
