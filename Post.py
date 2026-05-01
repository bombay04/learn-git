import requests
import json

url = "https://reqres.in/api/collections/products/records?project_id=17402"

payload = json.dumps({
  "data": {
    "name": "kaijeaw",
    "price": 150,
    "category": "Food",
    "in_stock": True
  }
})
headers = {
  'x-api-key': 'pro_d44b7123ff73b17cb971edb77223243099af1b58e94f8e6716e64f8c4a30eb05',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
