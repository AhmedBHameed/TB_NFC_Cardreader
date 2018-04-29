import environments
import requests
import json

class Http:
    # url = "https://jsonplaceholder.typicode.com/"
    url = environments.backendUrlHome
    http = requests
    headers = {'Content-type': 'application/json'}

    def __init__(self):
      print ('HTTP module initialized')
    def get(self, page=''):
        return self.http.get(self.url + page).json()
        
    def post(self, page, nfcid):
        payload = payload || slef.query(nfcid)
        return self.http.post(self.url + page, data=json.dumps(payload), headers=self.headers).json()
    def query(nfcid):
        return {
            'variables': null,
            'query': 'mutation { trakMyAss(nfcid: "' + nfcid + '") { id, freelancer_id, partner_id, log_date, login, logout, notes, ack { ok, message } } }'
        }
        
http = Http()
print (http.post('posts', '1,2,3,4'))
