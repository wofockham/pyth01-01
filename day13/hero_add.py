import requests

response = requests.post('http://localhost:5000/api/heroes',
                         data={"person": "Charlotte"})
print(response.text)
