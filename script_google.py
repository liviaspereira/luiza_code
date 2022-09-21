'''Criar um script google que retorna se o site google está acessivel ou não.'''

import requests

try:
    resposta = requests.get("https://www.google.com")
    if resposta.ok:
        print("Site está acessível")
    else:
        print("Site não está acessível")

except(Exception):
    print("Site não está acessível")

