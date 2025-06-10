import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        return response.content ##return bytes: b'[{"name": "Daniel", ...}]'
        #return response.json() ##return parsed json: [{"name": "Daniel", ...}]
        #return response.text ##return str: '[{"name": "Daniel", ...}]'
        


    def load_json(self):
        data = self.get_response_body()
        return json.loads(data) ##parsed json: [{"name": "Daniel", ...}]



# url = "https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json"
# requester = GetRequester(url)


# data = requester.get_response_body()
# for person in data:
#     print(f"{person['name']} is a {person['occupation']}")