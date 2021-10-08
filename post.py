import requests
import json
r=requests.post("https://httpbin/post",data={"name":"neeraj"})
print("Headers:",r.headers)
print(r.text)