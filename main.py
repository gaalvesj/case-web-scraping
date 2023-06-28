from bs4 import BeautifulSoup
import requests

URL = 'https://agostinholeiloes.com.br/'  # substitua pela URL desejada
response = requests.get(URL)

# Criar um objeto BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Encontrar todas as tags 'b'
tags_b = soup.find('b')

tags_h4 = soup.find('h6', class_='card-title m-0').text

tags_p = soup.find('p', class_= 'mb-0').text;

print(f"o valor de avaliação é de: {tags_b}");
print(tags_h4)
print(tags_p)