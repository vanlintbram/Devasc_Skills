import requests

access_token = 'MjU3MDJiOWYtNmIwZi00MTcwLTkzMDUtNzU4NTg2ZmE4ZWY0ZWFhNWFjZDgtMDNm_PF84_consumer'
room_id = 'Y2lzY29zcGFyazovL3VzL1JPT00vNmQ5MWVkODAtYTJjMS0xMWViLWI4ZWItYTljZTkzYjg3ZWRl'
person_email = 'alain.pieters@biasc.be'
url = 'https://webexapis.com/v1/memberships'
headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
}
params = {'roomId': room_id, 'personEmail': person_email}
res = requests.post(url, headers=headers, json=params)
print(res.json())