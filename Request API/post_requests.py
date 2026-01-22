# Body (Post) request

# Creating Information

import requests

url = "https://jsonplaceholder.typicode.com/posts"

# body data
payload = {
    "title": "Hello from Python",
    "body": "This is a test post",
    "userId": 1,
}

response = requests.post(url, json=payload)

print("Status code:", response.status_code)
data = response.json()
print(data)
