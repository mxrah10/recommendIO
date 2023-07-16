from dotenv import load_dotenv
import os
import requests

response = requests.get('https://api.jikan.moe/v4/anime?q=&sfw')

for data in response.json()['data']:
    print (data['title'])