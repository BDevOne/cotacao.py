import requests
from tkinter import *


def pegar_cotacoes():
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL,GBP-BRL,ETH-BRL") 

    requisicao_dic = requisicao.json()

    cotacao_dolar = requisicao_dic['USDBRL']['bid']
    cotacao_euro = requisicao_dic['EURBRL']['bid']
    cotacao_btc = requisicao_dic['BTCBRL']['bid']
    cotacao_libra = requisicao_dic['GBPBRL']['bid']
    cotacao_eth = requisicao_dic['ETHBRL']['bid']

    texto = f'''
    Dolar: {cotacao_dolar}
    Euro: {cotacao_euro}
    Libra: {cotacao_libra}
    BTC: {cotacao_btc}
    Ethereum: {cotacao_eth}'''
    


    texto_cotacoes["text"] = texto

janela = Tk()
janela.title("Cotação do câmbio")

#Cotação Moedas

texto_orientacao = Label(janela, text="Clique para buscar cotação atual do câmbio")
texto_orientacao.grid(column=0, row=0, padx=10, pady=10)

botao = Button(janela, text="Buscar cotações diária", command=pegar_cotacoes,  background='red', foreground='white')
botao.grid(column=0, row=1, padx=10, pady=10)

texto_cotacoes = Label(janela, text="Aparecer câmbio atual")
texto_cotacoes.grid(column=0, row=2, padx=10, pady=10)


janela.mainloop()