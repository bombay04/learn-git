import requests

url = "https://reqres.in/api/collections/products/records"

payload = {}
headers = {
  'x-api-key': 'pub_73d7c015ce95a15cd03d4c867a40285748a5e461cab4f074297ee91e15c629b8',
  'Authorization': 'Bearer {{GIT_TOKEN}}'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
