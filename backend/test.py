from dotenv import load_dotenv
import os
import requests

response = requests.get('https://api.jikan.moe/v4/top/anime')

i = 0
for data in response.json()['data']:
    print (data['title'])
    i+=1
print (i)