import requests

url = "http://localhost:8000/embed"
files = {'file': open('../robot.jpeg', 'rb')}
response = requests.post(url, files=files)
print(response.json())