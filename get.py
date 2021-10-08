import requests
import json
r=requests.get("https://httpbin.org/cache")

print("Headers:",r.headers)