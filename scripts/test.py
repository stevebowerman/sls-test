import requests

url = "https://kxiaa6psk1.execute-api.eu-west-1.amazonaws.com/dev/mpan"
mpan = "1"

r = requests.get(url + "/" + mpan)

print(r.json())
