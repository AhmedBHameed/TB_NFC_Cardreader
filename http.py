import environments
import requests
import json

class Http:
    url = "https://jsonplaceholder.typicode.com/"
    # url = environments.backendUrl
    http = requests
    headers = {'Content-type': 'application/json'}

    def __init__(self):
      print ('HTTP module initialized')
    def get(self, page=''):
        return self.http.get(self.url + page).json()
        
    def post(self, page, payload):
        return self.http.post(self.url + page, data=json.dumps(payload), headers=self.headers).json()
        
http = Http()
print (http.post('posts', {'userId':1, 'id': 101, 'title': 'this is a new title', 'body': 'This is my new body'}))
