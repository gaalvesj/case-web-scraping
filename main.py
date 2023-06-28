import requests
from lxml import html

URL = 'https://agostinholeiloes.com.br/'
response = requests.get(URL)


tree = html.fromstring(response.content)

resultado = tree.xpath('/html/body/div[1]/div[3]/div[2]/div[5]/div/div/div/a/p[1]/small')


for r in resultado:
    print(r.text)
