import requests
from bs4 import BeautifulSoup
import os
import time
import urllib3
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

load_dotenv()
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def scrape_ethiojobs():
    url = "https://ethiojobs.net/jobs?searchId=1713869642.8572&action=search&keywords=IT&search=IT"
    print(f"[INFO] Scraping Ethiojobs with Selenium: {url}")
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    jobs = []
    driver.implicitly_wait(10)
    job_cards = driver.find_elements(By.CSS_SELECTOR, 'div.MuiGrid-item.MuiGrid-grid-xs-12')
    print(f"[DEBUG] Found {len(job_cards)} job card elements.")
    for idx, card in enumerate(job_cards):
        try:
            # Extract job title
            title_elem = card.find_element(By.CSS_SELECTOR, 'a > p.MuiTypography-root')
            title = title_elem.text.strip()
            # Extract job link
            link_elem = card.find_element(By.CSS_SELECTOR, 'a')
            link = link_elem.get_attribute('href')
            if link and link.startswith('/'):
                link = f"https://www.ethiojobs.net{link}"
            # Extract company (look for button inside a[href*='/companies/'])
            company = None
            company_btns = card.find_elements(By.CSS_SELECTOR, "a[href*='/companies/'] > button")
            if company_btns:
                company = company_btns[0].text.strip()
            # Only add if all fields are present
            if title and company and link:
                print(f"[INFO] Found job: {title} at {company} ({link})")
                jobs.append({
                    "title": title,
                    "company": company,
                    "link": link
                })
        except Exception as e:
            continue
    driver.quit()
    print(f"[INFO] Ethiojobs: {len(jobs)} jobs extracted.")
    return jobs

def scrape_employethiopia():
    url = "https://www.employethiopia.com/search-jobs/IT"
    print(f"[INFO] Scraping EmployEthiopia: {url}")
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    response = requests.get(url, headers=headers, verify=False)
    soup = BeautifulSoup(response.text, "html.parser")
    jobs = []
    # TODO: Implement EmployEthiopia extraction logic
    print("[DEBUG] EmployEthiopia extraction not yet implemented.")
    return jobs

def scrape_jobwebethiopia():
    url = "https://www.jobwebethiopia.com/job-category/it-computer-jobs-in-ethiopia/"
    print(f"[INFO] Scraping JobWeb Ethiopia: {url}")
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    jobs = []
    # TODO: Implement JobWeb Ethiopia extraction logic
    print("[DEBUG] JobWeb Ethiopia extraction not yet implemented.")
    return jobs

def scrape_myjobo():
    url = "https://www.myjobo.com/jobs/ethiopia/it"
    print(f"[INFO] Scraping MyJobo: {url}")
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    jobs = []
    # TODO: Implement MyJobo extraction logic
    print("[DEBUG] MyJobo extraction not yet implemented.")
    return jobs

def scrape_jobs():
    all_jobs = []
    all_jobs.extend(scrape_ethiojobs())
    all_jobs.extend(scrape_employethiopia())
    all_jobs.extend(scrape_jobwebethiopia())
    all_jobs.extend(scrape_myjobo())
    print(f"[INFO] Total jobs scraped from all sources: {len(all_jobs)}")
    return all_jobs
