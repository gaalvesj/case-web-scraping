import requests
from lxml import html
import re

def imgLink():

    URL = 'https://agostinholeiloes.com.br/item/1435/detalhes?page=1'

    response = requests.get(URL)
    tree = html.fromstring(response.content)

    style = tree.xpath('/html/body/div[1]/div[2]/div[2]/div/div/div[2]/a/div/@style')[0]

    url_imagem_rel = re.search('url\((.*?)\)', style).group(1)

    if url_imagem_rel.startswith('/'):
        url_imagem = f"https://agostinholeiloes.com.br{url_imagem_rel}"
    else:
        url_imagem = url_imagem_rel

    print(f"o link da imagem é: {url_imagem}")
 