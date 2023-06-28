import requests
from lxml import html
from imovePage import extrairEndereco
from docExtract import extraiLink
from imgExtract import imgLink

def extraiPaginaPrincipal():
    URL = 'https://agostinholeiloes.com.br/'
    response = requests.get(URL)
    tree = html.fromstring(response.content)


    valorLance = tree.xpath('/html/body/div[1]/div[3]/div[2]/div[5]/div/div/div/a/p[1]/small')
    titulo = tree.xpath('/html/body/div[1]/div[3]/div[2]/div[5]/div/div/a[1]/h6')
    dataPrimeira = tree.xpath('/html/body/div[1]/div[3]/div[2]/div[5]/div/div/div/a/p[1]/text()')
    valorSegundoLance = tree.xpath('/html/body/div[1]/div[3]/div[2]/div[5]/div/div/div/a/p[2]/small')


    for i in titulo:
        print(f"O titulo do lote é: {i.text}")

    for i in valorLance:
        print(i.text)

    for i in dataPrimeira:
        print(f"a data do primeiro leilão é:{i}")

    for i in valorSegundoLance:
        print(f"o valor do segundo leilão é: {i.text}")
    
    return



extraiPaginaPrincipal()
extrairEndereco()
extraiLink()
imgLink()