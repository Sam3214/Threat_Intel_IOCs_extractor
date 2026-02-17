import requests

def ioc_url_get(threat_url):
  url = "https://api.iocparser.com/url"

  payload = {"url": threat_url}
  headers = {'Content-Type': 'application/json'}
  response = requests.request("POST", url, headers=headers, json=payload)
  return response.json()
