import requests
r = requests.delete('https://httpbin.org/delete')
print("Header: ",r.headers)
print(r.text)