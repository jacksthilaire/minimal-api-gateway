import requests

# POST request
print("POST REQUEST add USER")
res = requests.post("http://localhost:8000/users/", json={"name": "Test1", "email": "Test1@example.com"})
print(res.json())

# GET all users
print("GET REQUEST all USERS")
res = requests.get("http://localhost:8000/users/")
print(res.json())

# GET specific user
print("GET REQUEST specific USER")
res = requests.get("http://localhost:8000/users/1")
print(res.json())
