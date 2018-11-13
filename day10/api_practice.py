import requests

response = requests.get('http://api.open-notify.org/astros.json')
response_data = response.json() # This turns the returned JSON text into a Python dictionary.

# print(response_data)

# {"people": [{"name": "Sergey Prokopyev", "craft": "ISS"}, {"name": "Alexander Gerst", "craft": "ISS"}, {"name": "Serena Aunon-Chancellor", "craft": "ISS"}], "message": "success", "number": 3}

for key, value in response_data.items():
    print("Key:", key, "Value:", value, "\n")

# Iterating through the list under the key of "people"
for astronaut in response_data["people"]:
    print(astronaut["name"])
