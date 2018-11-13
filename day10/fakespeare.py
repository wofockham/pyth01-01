import requests

response = requests.get('http://ShakeItSpeare.com/api/poem')
data = response.json()
poem = data["poem"]

print(poem)

# Fancy smug way:
# poem = response.json()["poem"]
