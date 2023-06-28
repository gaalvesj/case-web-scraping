import requests
from lxml import html

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


def imovelPage():
    URL = 'https://agostinholeiloes.com.br/item/1435/detalhes?page=1'
    response = requests.get(URL)
    tree = html.fromstring(response.content)

    enderecoImovel = tree.xpath('/html/body/div[1]/div[2]/div[4]/div[2]/div/p')
    for i in enderecoImovel:
        print(f"o endereço do imovel é: {i.text}")
        return
imovelPage()