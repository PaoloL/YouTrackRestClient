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
issues = project.get_issues(limit=None)
print(f"Found {len(issues)} issues")
for issue in issues:
    print(f"{issue['id']}: {issue['summary']}:  {issue['description']}")
issue = Issue(client, 'AI-121')
issue.add_spent_time(60)