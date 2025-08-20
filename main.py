import requests
from send_email import sendemail

url=("https://newsapi.org/v2/everything?q=tesla&from="
     "2025-07-20&sortBy=publishedAt&apiKey=0e702423"
     "8a674610911c037b16ee9d48"
    )
api_key='0e7024238a674610911c037b16ee9d48'

r=requests.get(url)
content=r.json()

body= ""
for i in content["articles"]:
    body = body + i["title"] + "\n" + i["description"] + "\n\n"

sendemail(msg=body)