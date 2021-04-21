import requests
import json

access_token = 'MjU3MDJiOWYtNmIwZi00MTcwLTkzMDUtNzU4NTg2ZmE4ZWY0ZWFhNWFjZDgtMDNm_PF84_consumer'
url = 'https://webexapis.com/v1/people/me'
headers = {
    'Authorization': 'Bearer {}'.format(access_token)
}
res = requests.get(url, headers=headers)
print(json.dumps(res.json(), indent=4))
