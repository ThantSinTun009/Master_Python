import requests

url = "https://reqres.in/api/users"
params = {"page": 2}

response = requests.get(url, params=params)
print("Final url:", response.url)

response.raise_for_status() # raises error for 4xx/5xx

data = response.json() # into python dict
print("Page:", data["page"])
for user in data["data"]:
    print(user["email"])


""" Will raise error because reqres.in recently started blocking some requests. So the server returns:"""