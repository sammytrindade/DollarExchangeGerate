# Dollar to Real Exchange Rate

This Python script fetches the current Dollar to Real exchange rate from Google and displays it using a Tkinter graphical interface.

## Prerequisites

Make sure to have the following libraries installed:

```bash
pip install requests
pip install beautifulsoup4
```

## How to Use

1. Run the script.
2. Click the "Generate Exchange Rate" button.
3. The Dollar to Real exchange rate will be displayed in the graphical interface.

## Code Details

- The request link is set to "https://www.google.com/search?q=Cotacao+do+dolar+hoje."
- The `request` header contains a User-Agent simulating a web browser.
- The HTML of the page is parsed using the `BeautifulSoup` library.
- The Dollar exchange rate is extracted from the `HTML` using specific classes.
- The `Tkinter` graphical interface contains a button to trigger the `main` function, which makes the request and displays the exchange rate.
- If an error occurs during data extraction, an error message is displayed in the interface.

---
---
---

# Cotação do Dólar para Real

Este projeto em Python utiliza a biblioteca `requests` para fazer uma requisição `HTTP` ao site do Google e a biblioteca `BeautifulSoup` para realizar o parsing do `HTML`, extraindo informações sobre a cotação do Dólar para Real. 
Além disso, o `Tkinter` é utilizado para criar uma interface gráfica simples que exibe a cotação.

## Pré-requisitos

Certifique-se de ter as seguintes bibliotecas instaladas:

```bash
pip install requests
pip install beautifulsoup4
```

## Como usar

1. Execute o script.
2. Clique no botão "Gerar cotação".
3. A cotação do Dólar para Real será exibida na interface gráfica.

## Detalhes do Código

- O link da requisição é definido como "https://www.google.com/search?q=Cotacao+do+dolar+hoje".
- O cabeçalho da requisição contém um User-Agent simulando um navegador web.
- O `HTML` da página é analisado utilizando a biblioteca `BeautifulSoup`.
- A cotação do Dólar é extraída do `HTML` usando as classes específicas.
- A interface gráfica `Tkinter` contém um botão para acionar a função `main` que faz a requisição e exibe a cotação.
- Caso ocorra algum erro durante a extração de dados, uma mensagem de erro é exibida na interface.


