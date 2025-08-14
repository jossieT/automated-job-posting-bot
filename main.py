from job_scraper.scraper import scrape_jobs
from telegram_poster.poster import post_to_channel
from utils.deduplicator import is_duplicate, save_posted
import time

def main():
    print("[INFO] Starting job scraping...")
    jobs = scrape_jobs()
    print(f"[INFO] {len(jobs)} jobs scraped.")
    batch_size = 5
    delay_seconds = 5 * 60 * 60  # 5 hours
    jobs_to_post = [job for job in jobs if not is_duplicate(job['link'])]
    print(f"[INFO] {len(jobs_to_post)} new jobs to post.")
    for i in range(0, len(jobs_to_post), batch_size):
        batch = jobs_to_post[i:i+batch_size]
        print(f"[INFO] Posting batch {i//batch_size+1} ({len(batch)} jobs)...")
        for job in batch:
            print(f"[INFO] Posting job to Telegram: {job['title']} at {job['company']}")
            post_to_channel(job)
            print(f"[INFO] Saving posted job: {job['link']}")
            save_posted(job['link'])
        if i + batch_size < len(jobs_to_post):
            print(f"[INFO] Sleeping for {delay_seconds/3600} hours before next batch...")
            time.sleep(delay_seconds)
    print("[INFO] All jobs posted.")

if __name__ == "__main__":
    main()
