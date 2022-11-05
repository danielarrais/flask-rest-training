import requests

BASE_URL = "http://127.0.0.1:5000/"

response = requests.get(f"{BASE_URL}/helloworld/daniel")
print(response.json())

response = requests.put(f"{BASE_URL}/video/1", {
    "views": 10000,
    "name": "Teste",
    "likes": 100
})
print(response.json())