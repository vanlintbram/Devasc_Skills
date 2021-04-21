import requests

access_token = 'MjU3MDJiOWYtNmIwZi00MTcwLTkzMDUtNzU4NTg2ZmE4ZWY0ZWFhNWFjZDgtMDNm_PF84_consumer'
url = 'https://webexapis.com/v1/rooms'
headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
}
params={'title': 'netacad_devasc_skills_BVL'}
res = requests.post(url, headers=headers, json=params)
print(res.json())