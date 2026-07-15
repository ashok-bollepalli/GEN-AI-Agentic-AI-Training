import requests

url = "https://jsonplaceholder.typicode.com/users"

params = {
    "uname " : "ashokit",
    "password" : "ashokit@123"
}

headers = {
    "X-API-Key" : "Your_secret_key"
}

response = requests.get(url, headers = headers)

students = response.json()

for s in students:
    print(s)

