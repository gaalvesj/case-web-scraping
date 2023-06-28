import requests
from lxml import html

URL = 'https://agostinholeiloes.com.br/item/1435/detalhes?page=1'
response = requests.get(URL)
tree = html.fromstring(response.content)

enderecoImovel = tree.xpath('/html/body/div[1]/div[2]/div[4]/div[2]/div/p//text()')

if len(enderecoImovel) >= 2:
    endereco = enderecoImovel[2].strip()
    primeiraLinha = endereco.split('\n')[0]
    print(f"o endereço do imovel é: {primeiraLinha}")
else:
    print("Não foi possível encontrar o endereço do imóvel.")

