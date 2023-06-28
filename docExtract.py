import requests
from lxml import html

def extraiLink():
    URL = 'https://agostinholeiloes.com.br/item/1435/detalhes?page=1'
    response = requests.get(URL)
    tree = html.fromstring(response.content)
# Localiza a URL do documento usando o XPath fornecido
    url_documento_rel = tree.xpath('/html/body/div[1]/div[2]/div[3]/div[7]/p[2]/a/@href')[0]

# Verifica se a URL é relativa
    if url_documento_rel.startswith('/'):
        url_documento = f"https://agostinholeiloes.com.br{url_documento_rel}"
    else:
        url_documento = url_documento_rel

    print(f"o link do documento é: {url_documento}") 
    return
extraiLink()