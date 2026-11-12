
import json
import os
import urllib.request
from pathlib import Path
from datetime import datetime, timezone

USERNAME = "Adnan-X786"
TOKEN = os.getenv("GH_TOKEN")

if not TOKEN:
    raise SystemExit("GitHub token missing. Set GH_TOKEN first.")

query = """
query($login: String!) {
  user(login: $login) {
    contributionsCollection {
      contributionCalendar {
        totalContributions
        weeks {
          contributionDays {
            date
            contributionCount
          }
        }
      }
    }
  }
}
"""

payload = {
    "query": query,
    "variables": {"login": USERNAME}
}

request = urllib.request.Request(
    "https://api.github.com/graphql",
    data=json.dumps(payload).encode(),
    headers={
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json",
        "User-Agent": "Adnan-GitHub-Profile"
    }
)

with urllib.request.urlopen(request) as response:
    result = json.loads(response.read())

if "errors" in result:
    raise SystemExit(result["errors"])

calendar = result["data"]["user"]["contributionsCollection"]["contributionCalendar"]

output = {
    "username": USERNAME,
    "total_contributions": calendar["totalContributions"],
    "updated_at": datetime.now(timezone.utc).isoformat(),
    "weeks": calendar["weeks"]
}

destination = Path(__file__).resolve().parent.parent / "data" / "contributions.json"
destination.parent.mkdir(exist_ok=True)

destination.write_text(
    json.dumps(output, indent=2),
    encoding="utf-8"
)

print("Contribution data saved successfully!")
print("Total contributions:", calendar["totalContributions"])
print("File:", destination)
