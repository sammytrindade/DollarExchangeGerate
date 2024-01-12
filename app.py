import requests
from bs4 import BeautifulSoup
from tkinter import *


def main():

    link = "https://www.google.com/search?q=Cotacao+do+dolar+hoje"
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36"
    }
    request = requests.get(link, headers=headers)
    # print(request)
    site = BeautifulSoup(request.text, "html.parser")

    title = site.find("title")
    print(title.get_text(), "\n")

    try:
        valueDolar = site.find("span", class_="DFlfde")
        valueBrazil = site.find("span", class_="SwHCTb")

        text = f"""
                {valueDolar.getText()} Dólar Americano na cotação de hoje:
                Valor com precisão: R${valueBrazil["data-value"]}
                Valor arredondado: R${valueBrazil.get_text()}"""
    except AttributeError as e:
        text = f"Erro: {e}"
    textExchange["text"] = text


window = Tk()
window.title(title.get_text())

window.mainloop()