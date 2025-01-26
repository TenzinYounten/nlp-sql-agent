import requests

url = "http://localhost:8000/query"
payload = {"query": "How many orders have not synced today?"}
response = requests.post(url, json=payload)
print(response.json())