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
import random
from modulos.identificador import *



banner='''
 _____  _  _
|  ___|| |(_)
| |__  | | _  ____ __ _
|  __| | || ||_  // _` |
| |___ | || | / /| (_| |
\____/ |_||_|/___|\__,_|


Bem vindo a Eliza, sua assistente pessoal
Digite ajuda para ver a documentação
'''

mensagem_eliza='\nComo posso te ajudar?\n~$ '

diretorio_atual=os.getcwd()



def menu():
    inicio=1
    lista=[]
    if(inicio==1):
        inicio=0
        print('checando todas as dependências\n')
        os.system('./compilar.sh')




    while True:
        try:
            os.chdir(diretorio_atual)
            frase=raw_input(mensagem_eliza)
        except NameError:
            os.chdir(diretorio_atual)
            frase=input(mensagem_eliza)
        frase=frase.lower()
        lista.append(frase)
        identifica(frase,lista)

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
