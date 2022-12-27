import requests
url = "http://172.17.0.2:5000/hi"
response = requests.get(url=url)
print(response.text)