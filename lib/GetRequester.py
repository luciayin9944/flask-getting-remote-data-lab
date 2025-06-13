import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        return response.content ##return bytes: b'[{"name": "Daniel", ...}]'
    
    """
        #return response.json() ##return parsed json: [{"name": "Daniel", ...}]
        #return response.text ##return str: '[{"name": "Daniel", ...}]'
    """

    def load_json(self):
        data = self.get_response_body()
        return json.loads(data) ##parsed json: [{"name": "Daniel", ...}]

