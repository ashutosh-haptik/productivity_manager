import requests
import os
from dotenv import load_dotenv

load_dotenv(".env")
pr_url = "https://github.com/hellohaptik/HaptikLabs.Kiwi.CoreAPIs/pull/11921/files"

resp = requests.get(
    pr_url,
    headers={
        "Authorization": f"Bearer {os.environ.get("GITHUB_TOKEN")}"
    }
)

print(resp.text)