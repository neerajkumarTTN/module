import requests
r = requests.put('https://httpbin.org/put', data = {'name':'Neeraj'})
print("Headers:",r.headers)
print(r.text)