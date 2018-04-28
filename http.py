import environments
import requests

class Http:
    # url = "https://jsonplaceholder.typicode.com/"
    url = environments.backendUrl
    http = requests
    headers = {'Content-type': 'application/json'}

    def __init__(self):
      print ('HTTP module initialized')
    def get(self, page=''):
        return self.http.get(self.url + page).json()
        
    def post(self, data):
        return self.http.get(self.url + page, data, headers=self.headers).json()
        
http = Http()
http.get('posts')