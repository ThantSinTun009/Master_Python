# Basic request demo

import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

response = requests.get(url)

print("Status code:", response.status_code)
print("Content-Type:", response.headers.get("Content-Type"))


data = response.json() # parse JSON into a Python dict

# print(data)

print("Post title:", data["title"])
