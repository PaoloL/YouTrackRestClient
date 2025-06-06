import requests

class Project:
    def __init__(self, client, project_id):
        """
        Initialize Project object.
        
        Args:
            client: YouTrackClient instance
            project_id: ID of the project (e.g., 'AI')
        """
        self.client = client
        self.project_id = project_id
    
    #implement GET /api/admin/projects/{projectID}?{fields}
    def get_details(self):

        url = f"{self.client.base_url}/api/admin/projects/{self.project_id}"
        params = {
            'fields': 'id,name,description,created',
            'project': self.project_id
        }
            
        response = requests.get(url, headers=self.client.headers, params=params)
        response.raise_for_status()
        
        return response.json()
    
    #Implement GET /api/issues?{fields}&{$top}&{$skip}&{query}&{customFields}
    def get_issues(self, limit=None):
        
        url = f"{self.client.base_url}/api/issues"
        params = {
            'fields': 'id,summary,description',
            'query': f"project: {self.project_id}",
            '$top': limit,
        }
            
        response = requests.get(url, headers=self.client.headers, params=params)
        response.raise_for_status()
        
        return response.json()