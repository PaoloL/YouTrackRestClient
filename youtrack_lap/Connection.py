import requests

class Connection:
    def __init__(self, base_url, token):
        """
        Initialize YouTrack client.
        
        Args:
            base_url: YouTrack instance URL (e.g., 'https://example.youtrack.cloud')
            token: Permanent token for authentication
        """
        self.base_url = base_url.rstrip('/')
        self.headers = {
            'Authorization': f'Bearer {token}',
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Cache-Control': 'no-cache'
        }
    
    #Implement GET /api/admin/projects?{fields}&{$top}&{$skip}
    def get_projects(self, limit=None, skip=None):
        url = f"{self.base_url}/api/admin/projects"
    
        params = {
            'fields': 'id,name,shortName,createdBy(name)',
            '$top': limit,
            '$skip': skip
        }
        
        response = requests.get(url, headers=self.headers, params=params)
        response.raise_for_status()  # Raise exception for HTTP errors
        
        return response.json()
