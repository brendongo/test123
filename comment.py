import requests
import sys

def main():
    session = requests.Session()
    session.headers["Authorization"] = f"token {sys.argv[1]}"
    url = f"https://api.github.com/repos/returntocorp/semgrep/pulls/{sys.argv[2]}/comments"
    print(url)
    message = "Test message"

    pr_comment_payload = {
        "body": message,
        "commit_id": sys.argv[3]
    }
    print(pr_comment_payload)

    r = session.post(url,json=pr_comment_payload)
    print(r.status_code)
    r.raise_for_status()


main()