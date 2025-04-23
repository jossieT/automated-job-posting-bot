import json
from pathlib import Path

DATA_FILE = Path("data/posted_jobs.json")

def is_duplicate(link):
    if not DATA_FILE.exists():
        return False
    with open(DATA_FILE, "r") as f:
        posted = json.load(f)
    return link in posted

def save_posted(link):
    posted = []
    if DATA_FILE.exists():
        with open(DATA_FILE, "r") as f:
            posted = json.load(f)
    posted.append(link)
    with open(DATA_FILE, "w") as f:
        json.dump(posted, f)
