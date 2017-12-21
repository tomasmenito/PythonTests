import json,requests,sys

url ='https://api.github.com//users//mralexgray//repos'
response = requests.get(url)
response.raise_for_status()

data = json.loads(response.text)
w = data['list']
print(w)
