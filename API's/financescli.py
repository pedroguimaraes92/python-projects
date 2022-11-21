import os
import time
import requests
import json
import colored
from colored import fg

while True:
    os.system('cls' if os.name == 'nt' else 'clear') #clear the terminal
    print("Acompanhe em tempo real:\n\n")

    cotacoes = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL,ETH-BRL")
    cotacoes = cotacoes.json()
    dolar_compra = cotacoes['USDBRL']["bid"]
    dolar_venda = cotacoes['USDBRL']["ask"]
    (dolar_var) = cotacoes['USDBRL']["varBid"]
    dolar_perc = cotacoes['USDBRL']["pctChange"]
    euro_compra = cotacoes['EURBRL']["bid"]
    euro_venda = cotacoes['EURBRL']["ask"]
    euro_var = cotacoes['EURBRL']["varBid"]
    euro_perc = cotacoes['EURBRL']["pctChange"]
    bitcoin_compra = cotacoes['BTCBRL']["bid"]
    bitcoin_venda = cotacoes['BTCBRL']["ask"]
    bitcoin_var = cotacoes['BTCBRL']["varBid"]
    bitcoin_perc = cotacoes['BTCBRL']["pctChange"]
    eth_compra = cotacoes['ETHBRL']["bid"]
    eth_venda = cotacoes['ETHBRL']["ask"]
    eth_var = cotacoes['ETHBRL']["varBid"]
    eth_perc = cotacoes['ETHBRL']["pctChange"]
    #print(cotacoes)

    red = fg('red')
    purple = fg('dark_violet_1b')
    yellow = fg('yellow')
    green = fg('green')
    white = fg('white')
    orange = fg('dark_orange')
    lgreen = fg('light_green_2')
    nred = fg('red_3a')

    print(green + "Dólar:")
    print(white + "Compra:",white + "R$", green + (dolar_compra))
    print(white + "Venda:",white + "R$", green + (dolar_venda))
    if float(dolar_var) > 0:
        print(white + "Variação:",white + "R$", lgreen + (dolar_var))
    else:
        print(white + "Variação:",white + "R$", nred + (dolar_var))

    if float(dolar_perc) > 0:
        print(white + "Porcentagem:", lgreen + "+",(dolar_perc),"%\n")
    else:
        print(white + "Porcentagem:", nred + (dolar_perc),"%\n")

    print(orange + "Euro:")
    print(white + "Compra:",white + "R$", orange + (euro_compra))
    print(white + "Venda:",white + "R$", orange + (euro_venda))
    if float(euro_var) > 0:
        print(white + "Variação:",white + "R$", lgreen + (euro_var))
    else:
        print(white + "Variação:",white + "R$", nred + (euro_var))

    if float(euro_perc) > 0:
        print(white + "Porcentagem:", lgreen + "+",(euro_perc),"%\n")
    else:
        print(white + "Porcentagem:", nred + (euro_perc),"%\n")

    print(yellow + "Bitcoin:")
    print(white + "Compra:",white + "R$", yellow + (bitcoin_compra))
    print(white + "Venda:", white + "R$", yellow + (bitcoin_venda))
    if float(bitcoin_var) > 0:
        print(white + "Variação:",white + "R$", lgreen + (bitcoin_var))
    else:
        print(white + "Variação:",white + "R$", nred + (bitcoin_var))

    if float(bitcoin_perc) > 0:
        print(white + "Porcentagem:", lgreen + "+",(bitcoin_perc),"%\n")
    else:
        print(white + "Porcentagem:", nred + (bitcoin_perc),"%\n")

    print(purple + "Ethereum:")
    print(white + "Compra:",white + "R$", purple +(eth_compra))
    print(white + "Venda:",white + "R$", purple +(eth_venda))
    if float(eth_var) > 0:
        print(white + "Variação:",white + "R$", lgreen + (eth_var))
    else:
        print(white + "Variação:",white + "R$", nred + (eth_var))

    if float(eth_perc) > 0:
        print(white + "Porcentagem:", lgreen + "+",(eth_perc),"%")
    else:
        print(white + "Porcentagem:", nred + (eth_perc),"%")
    print(white)
    time.sleep(15.5)
else:
    time.sleep(15)
