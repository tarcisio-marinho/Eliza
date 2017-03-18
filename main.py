#!/bin/bash/env python
# coding=UTF-8
# by Tarcisio marinho
# github.com/tarcisio-marinho

import requests
import json
import sys
import os
from datetime import datetime
from datetime import date



banner='''
 _____  _  _
|  ___|| |(_)
| |__  | | _  ____ __ _
|  __| | || ||_  // _` |
| |___ | || | / /| (_| |
\____/ |_||_|/___|\__,_|


Bem vindo a Eliza, sua assistente pessoal
'''

mensagem_eliza='\nOlá, como posso ajudar?\n~> '


#limpar tela
#API'S
#youtube- recomendados - novos videos
#twitch - principais streamers
#
#tocar(musica)
#ler(livro)
#criar(arquivo)
#youtube(nome_video)
#busca(google_nome)
#esvaziar_lixeira()
#atividades(){
#  print(atividades.txt)
#}
#ligarssh
# que horas sao

comandos='''
Olá, sou Eliza, uma assistente pessoal para linux!
Os comandos são:
*
*
*
*
*
*help imprime essa mensagem
'''
versao='Versão 1.0'

def identificador(frase):
    palavras=frase.split(' ')

    #Funcoes primarias
    if(frase=='quit' or frase=='sair' or frase=='exit' or frase=='vazar'):
        exit()

    elif(frase=='help' or frase=='ajuda' or frase=='tutorial' or frase=='list' or frase=='listar comandos' or frase=='listar'):
        print(comandos)

    elif(frase=='version' or frase=='versao' or frase=='versão' or frase=='-v' or frase=='--version'):
        print(versao)

    elif(frase=='limpar tela' or frase=='clear' or frase=='cls' or frase=='clear screen'):
        os.system('clear')

    elif(frase=='hora' or frase=='que horas sao?' or frase=='que horas sao' or frase=='que horas são?' or frase=='que horas são' or frase=='hora atual' or frase=='são que horas?' or frase=='sao que horas?' or frase=='sao que horas'):
        now=datetime.now()
        hora=now.hour
        minuto=now.minute
        segundo=now.second
        print "São: %s:%s:%s" % (hora,minuto,segundo)

    elif(frase=='que dia é hoje?' or frase=='que dia e hoje' or frase=='hoje é que dia?' or frase=='hoje e que dia'):
        now=datetime.now()
        ano=now.year
        mes=now.month
        dia=now.day
        hoje=date.today()
        if(hoje.weekday()==0):
            print('hoje é Segunda')
        elif(hoje.weekday()==1):
            print('hoje é Terça')
        elif(hoje.weekday()==2):
            print('hoje é Quarta')
        elif(hoje.weekday()==3):
            print('hoje é Quinta')
        elif(hoje.weekday()==4):
            print('hoje é Sexta')
        elif(hoje.weekday()==5):
            print('hoje é Sábado')
        elif(hoje.weekday()==6):
            print('hoje é Domingo')
        print "dia: %s do %s de %s" % (dia, mes, ano)




def menu():
    while True:
        try:
            frase=raw_input(mensagem_eliza)
        except NameError:
            frase=input(mensagem_eliza)
        frase=frase.lower()
        identificador(frase)

# MAIN
os.system('clear')
print(banner)
sair=None
try:
    menu()
except KeyboardInterrupt:
    try:
        sair=raw_input('\nDeseja sair ? ')
    except NameError:
        sair=input('\nDeseja sair ? ')
        if(sair=='sim' or sair=='1' or sair=='quit' or sair=='s' or sair=='exit'):
            print('Saindo...')
            exit()
        else:
            menu()
