import environments
import requests
import json

class Http:
    # url = "https://jsonplaceholder.typicode.com/"
    url = environments.backendUrl
    http = requests
    headers = {'Content-type': 'application/json'}

    def __init__(self):
      print ('HTTP module initialized')
    
    def get(self, page=''):
        return self.http.get(self.url + page).json()
        
    def post(self, page, payload):
          return self.http.post(self.url + page, data=json.dumps(self.query(payload)), headers=self.headers).json()
    
    def query(self, nfcid):
        return {
            'variables': None,
            'query': 'mutation { trackMyAss(nfcid: "' + nfcid + '") { id, freelancer_id, partner_id, log_date, login, logout, notes, ack { ok, message } } }'
        }
