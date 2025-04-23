import requests
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv

load_dotenv()

def scrape_jobs():
    url = os.getenv("JOB_SOURCE_URL")
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    jobs = []
    for item in soup.select("tr.job"):
        title = item.get("data-position")
        company = item.get("data-company")
        link = "https://remoteok.com" + item.get("data-url")
        if title and company:
            jobs.append({
                "title": title,
                "company": company,
                "link": link
            })
    return jobs
