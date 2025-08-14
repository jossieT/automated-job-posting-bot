import json
from pathlib import Path

DATA_FILE = Path("data/posted_jobs.json")

def is_duplicate(link):
    if not DATA_FILE.exists():
        print(f"[INFO] No posted jobs file found. Not a duplicate: {link}")
        return False
    with open(DATA_FILE, "r") as f:
        posted = json.load(f)
    is_dup = link in posted
    print(f"[INFO] Duplicate check for {link}: {is_dup}")
    return is_dup

def save_posted(link):
    posted = []
    if DATA_FILE.exists():
        with open(DATA_FILE, "r") as f:
            posted = json.load(f)
    posted.append(link)
    with open(DATA_FILE, "w") as f:
        json.dump(posted, f)
    print(f"[INFO] Saved posted job link: {link}")
