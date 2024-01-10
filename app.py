import requests
from bs4 import BeautifulSoup

link = "https://www.google.com/search?q=Cotacao+do+dolar+hoje"
headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36"
}
request = requests.get(link, headers=headers)
# print(request)
site = BeautifulSoup(request.text, "html.parser")

title = site.find("title")
print(title.get_text(), "\n")

valueDolar = site.find("span", class_="DFlfde")

print(valueDolar.getText(), "Dólar Americano na cotação de hoje:", "\n")

valueBrazil = site.find("span", class_="SwHCTb")

print("Valor com precisão: R$", valueBrazil["data-value"], sep=" ")

print("Valor arredondado: R$", valueBrazil.get_text(), sep=" ")
