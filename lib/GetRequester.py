import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(url=self.url)
        return response.content

    def load_json(self):
        data_list = []
        retrieved_data = json.loads(self.get_response_body())
        for response in retrieved_data:
            data_list.append(response)
        return data_list
    
get_requester = GetRequester('https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json')
print(get_requester.load_json())