import requests

url = "https://www.cloudnativeobservability.com"
resp = requests.get(url)
print(resp.status_code)
