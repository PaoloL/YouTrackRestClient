import os
from youtrack_lap.Connection import Connection
from youtrack_lap.Issue import Issue
from youtrack_lap.Project import Project

YOUTRACK_URL = "https://r3recube.myjetbrains.com/youtrack/"

def read_token_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read().strip()
    except FileNotFoundError:
        print(f"Token file not found: {file_path}")
        exit(1)
        return None

#Initialize the Authenticated Client
token_file = os.path.expanduser("secrets/yt_token.txt")
YOUTRACK_TOKEN = read_token_from_file(token_file)
client = Connection(base_url=YOUTRACK_URL, token=YOUTRACK_TOKEN)

project = Project(client, 'AI')
project_details = project.get_details()
project_issues = project.get_issues(limit=None)
print(f"Found {len(project_issues)} issues")
for issue in project_issues:
    print(f"{issue['id']}: {issue['summary']}:  {issue['description']}")

issue = Issue(client, 'AI-121')
issue_work_item = issue.get_work_items(limit=None)
print(f"Found {len(issue_work_item)} items")
for item in issue_work_item:
    #Convert {item['date']} from unepoch time to readable date
    from datetime import datetime
    timestamp_ms = item['date']
    date = datetime.fromtimestamp(timestamp_ms / 1000).strftime('%Y/%m/%d')

    print(f"User {item['author']['name']} spent {item['duration']['minutes']} minutes {item['$type']} on {date} for {item['text']}")
#issue.add_spent_time(60)