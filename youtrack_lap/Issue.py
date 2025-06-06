import requests
import datetime

class Issue:
    def __init__(self, client, issue_id):
        """
        Initialize Issue object.
        
        Args:
            client: YouTrackClient instance
            issue_id: ID of the issue (e.g., 'AI-123')
        """
        self.client = client
        self.id = issue_id
    
    def add_spent_time(self, duration, date=None, description=None):
        """
        Add spent time to the issue.
        
        Args:
            duration: Time spent in minutes or formatted string (e.g., '1h 30m')
            date: Date of work (defaults to today), format: YYYY-MM-DD
            description: Optional comment for the work item
            
        Returns:
            Response data from the API
        """
        # Format date if provided, otherwise use today
        if date is None:
            date = datetime.datetime.now().strftime("%Y-%m-%d")
        elif isinstance(date, datetime.datetime):
            date = date.strftime("%Y-%m-%d")
            
        # Prepare request data
        url = f"{self.client.base_url}/api/issues/{self.id}"

        data = {
            "duration": {
                "minutes": self._parse_duration(duration)
            },
            "date": date,
            "description" : description
        }
        
        # Make the API request
        response = requests.post(
            url, 
            headers=self.client.headers,
            json=data,
        )
        response.raise_for_status()
        
        return response.json()
    
    def _parse_duration(self, duration):
        """Convert duration string or minutes to minutes."""
        if isinstance(duration, int):
            return duration
            
        # Simple parsing for formats like "1h 30m" or "90m"
        total_minutes = 0
        
        if "h" in duration:
            hours_part = duration.split("h")[0].strip()
            total_minutes += int(hours_part) * 60
            duration = duration.split("h")[1]
            
        if "m" in duration:
            minutes_part = duration.split("m")[0].strip()
            if minutes_part:
                total_minutes += int(minutes_part)
                
        return total_minutes
