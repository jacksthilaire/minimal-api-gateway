import requests

# POST request
res = requests.post("http://localhost:8000/users/", data={"name": "Bob", "email": "bob@example.com"})
print(res.json())

# GET all users
res = requests.get("http://localhost:8000/users/")
print(res.json())

# GET specific user
res = requests.get("http://localhost:8000/users/1")
print(res.json())
