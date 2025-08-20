import requests

url=("https://newsapi.org/v2/everything?q=tesla&from="
     "2025-07-20&sortBy=publishedAt&apiKey=0e702423"
     "8a674610911c037b16ee9d48"
    )
api_key='0e7024238a674610911c037b16ee9d48'

r=requests.get(url)
content=r.json()

for i in content["articles"]:
    print(i["title"])
    print(i["description"])
    print("___________________________________________________________________________________________________________________________________________________")