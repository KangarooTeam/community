import requests
import json

a = requests.get('http://google.com')
print(a.content)
#result = json.loads(r.content.decode('utf-8'))