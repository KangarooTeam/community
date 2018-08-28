import requests
import json

a = requests.get('http://ipinfo.io/json')
result = json.loads(a.content.decode('utf-8'))
print(result)