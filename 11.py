from datetime import datetime
import requests


def url_caller(url):
    response = requests.get(url)
    if response.status_code == 200:
        print(f"{url} is ok")


for url in {'https://github.com', 'https://google.com', 'https://moshe.com'}:
    url_caller(url)
print(datetime.now())