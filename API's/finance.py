import os
import tkinter as tk
from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedTk
import time
from time import *
import json
import requests
import colored
from colored import fg




finance = ThemedTk(theme = "arc")
finance.geometry("1205x905")
finance.title("Finance API")
finance.iconbitmap('finance1.ico')
finance.resizable(False, False)
s = ttk.Style(finance)
bg = PhotoImage (file = 'finance.png')
s.configure(".", font = ('Roboto', 11))
label = Label(image = bg)
label.place (x = 0, y = 0)


cotacoes = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL,ETH-BRL")
cotacoes = cotacoes.json()
dolar_compra = cotacoes['USDBRL']["bid"]
dolar_venda = cotacoes['USDBRL']["ask"]
dolar_var = cotacoes['USDBRL']["varBid"]
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


#Dolar Labels


lbl_dolar_compra = Label(finance, font = ('Jura', 13), fg = '#FFFFFF', bg = '#464646')
lbl_dolar_compra.place(x = 420, y = 330)
lbl_dolar_compra.config(text = dolar_compra)

lbl_dolar_venda = Label(finance, font = ('Jura', 13), fg = '#FFFFFF', bg = '#464646')
lbl_dolar_venda.place(x = 585, y = 330)
lbl_dolar_venda.config(text = dolar_venda)

if float(dolar_perc) > 0:
    lbl_dolar_perc = Label(finance, font = ('Jura', 13), fg = '#39FF14', bg = '#464646')
    lbl_dolar_perc.place(x = 730, y = 330)
    lbl_dolar_perc.config(text = "+" + dolar_perc + "%")
else:
    lbl_dolar_perc = Label(finance, font = ('Jura', 13), fg = '#FF1A1A', bg = '#464646')
    lbl_dolar_perc.place(x = 730, y = 330)
    lbl_dolar_perc.config(text = dolar_perc + "%")

if float(dolar_var) > 0:
    lbl_dolar_var = Label(finance, font = ('Jura', 13), fg = '#39FF14', bg = '#464646')
    lbl_dolar_var.place(x = 850, y = 330)
    lbl_dolar_var.config(text = "+" + dolar_var)
else:
    lbl_dolar_var = Label(finance, font = ('Jura', 13), fg = '#FF1A1A', bg = '#464646')
    lbl_dolar_var.place(x = 850, y = 330)
    lbl_dolar_var.config(text = dolar_var)



#Euro Labels


lbl_euro_compra = Label(finance, font = ('Jura', 13), fg = '#FFFFFF', bg = '#464646')
lbl_euro_compra.place(x = 420, y = 430)
lbl_euro_compra.config(text = euro_compra)

lbl_euro_venda = Label(finance, font = ('Jura', 13), fg = '#FFFFFF', bg = '#464646')
lbl_euro_venda.place(x = 585, y = 430)
lbl_euro_venda.config(text = euro_venda)

if float(euro_perc) > 0:
    lbl_euro_perc = Label(finance, font = ('Jura', 13), fg = '#39FF14', bg = '#464646')
    lbl_euro_perc.place(x = 730, y = 430)
    lbl_euro_perc.config(text = "+" + euro_perc + "%")
else:
    lbl_euro_perc = Label(finance, font = ('Jura', 13), fg = '#FF1A1A', bg = '#464646')
    lbl_euro_perc.place(x = 730, y = 430)
    lbl_euro_perc.config(text = euro_perc + "%")

if float(euro_var) > 0:
    lbl_euro_var = Label(finance, font = ('Jura', 13), fg = '#39FF14', bg = '#464646')
    lbl_euro_var.place(x = 850, y = 430)
    lbl_euro_var.config(text = "+" + euro_var)
else:
    lbl_euro_var = Label(finance, font = ('Jura', 13), fg = '#FF1A1A', bg = '#464646')
    lbl_euro_var.place(x = 850, y = 430)
    lbl_euro_var.config(text = euro_var)

#Bitcon Labels


lbl_bitcoin_compra = Label(finance, font = ('Jura', 13), fg = '#FFFFFF', bg = '#464646')
lbl_bitcoin_compra.place(x = 420, y = 550)
lbl_bitcoin_compra.config(text = bitcoin_compra)

lbl_bitcoin_venda = Label(finance, font = ('Jura', 13), fg = '#FFFFFF', bg = '#464646')
lbl_bitcoin_venda.place(x = 585, y = 550)
lbl_bitcoin_venda.config(text = bitcoin_venda)

if float(bitcoin_perc) > 0:
    lbl_bitcoin_perc = Label(finance, font = ('Jura', 13), fg = '#39FF14', bg = '#464646')
    lbl_bitcoin_perc.place(x = 730, y = 550)
    lbl_bitcoin_perc.config(text = "+" + bitcoin_perc + "%")
else:
    lbl_bitcoin_perc = Label(finance, font = ('Jura', 13), fg = '#FF1A1A', bg = '#464646')
    lbl_bitcoin_perc.place(x = 730, y = 550)
    lbl_bitcoin_perc.config(text = bitcoin_perc + "%")

if float(bitcoin_var) > 0:
    lbl_bitcoin_var = Label(finance, font = ('Jura', 13), fg = '#39FF14', bg = '#464646')
    lbl_bitcoin_var.place(x = 850, y = 550)
    lbl_bitcoin_var.config(text = bitcoin_var)
else:
    lbl_bitcoin_var = Label(finance, font = ('Jura', 13), fg = '#FF1A1A', bg = '#464646')
    lbl_bitcoin_var.place(x = 850, y = 550)
    lbl_bitcoin_var.config(text = bitcoin_var)


#Ethereum Labels


lbl_eth_compra = Label(finance, font = ('Jura', 13), fg = '#FFFFFF', bg = '#464646')
lbl_eth_compra.place(x = 420, y = 670)
lbl_eth_compra.config(text = eth_compra)

lbl_eth_venda = Label(finance, font = ('Jura', 13), fg = '#FFFFFF', bg = '#464646')
lbl_eth_venda.place(x = 585, y = 670)
lbl_eth_venda.config(text = eth_venda)

if float(eth_perc) > 0:
    lbl_eth_perc = Label(finance, font = ('Jura', 13), fg = '#39FF14', bg = '#464646')
    lbl_eth_perc.place(x = 730, y = 670)
    lbl_eth_perc.config(text = "+" + eth_perc + "%")
else:
    lbl_eth_perc = Label(finance, font = ('Jura', 13), fg = '#FF1A1A', bg = '#464646')
    lbl_eth_perc.place(x = 730, y = 670)
    lbl_eth_perc.config(text = eth_perc + "%")

if float(eth_var) > 0:
    lbl_eth_var = Label(finance, font = ('Jura', 13), fg = '#39FF14', bg = '#464646')
    lbl_eth_var.place(x = 850, y = 670)
    lbl_eth_var.config(text = eth_var)
else:
    lbl_eth_var = Label(finance, font = ('Jura', 13), fg = '#FF1A1A', bg = '#464646')
    lbl_eth_var.place(x = 850, y = 670)
    lbl_eth_var.config(text = eth_var)



finance.mainloop()
