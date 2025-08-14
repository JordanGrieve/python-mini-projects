import json

import requests

url = 'https://api.languagetool.org/v2/check'
data = {
    'text': 'Tis is a nxe day',
    'language': 'auto',
}
response = requests.post(url, data=data)
results = json.loads(response.text)
print(results)

