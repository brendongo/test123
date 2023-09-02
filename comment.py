import requests
import sys
import json
from pathlib import Path
import os

def main():
    session = requests.Session()
    session.headers["Authorization"] = f"Token {sys.argv[1]}"
    url = f"https://api.github.com/repos/brendongo/test123/issues/{sys.argv[2]}/comments"
    session.headers[
        "Accept"
    ] = "application/vnd.github.comfort-fade-preview+json"
    print(url)
    message = "Test message"


    commit_id = json.loads(Path(os.getenv("GITHUB_EVENT_PATH")).read_text())["pull_request"]["head"]["sha"]
    pr_comment_payload = {
        "body": message,
        "commit_id": commit_id,
    }
    print(pr_comment_payload)

    r = session.post(url,json=pr_comment_payload)
    print(r.status_code)
    r.raise_for_status()


main()