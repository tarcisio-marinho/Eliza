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
import identificador



banner='''
 _____  _  _
|  ___|| |(_)
| |__  | | _  ____ __ _
|  __| | || ||_  // _` |
| |___ | || | / /| (_| |
\____/ |_||_|/___|\__,_|


Bem vindo a Eliza, sua assistente pessoal
Digite help para ver a documentação
'''

mensagem_eliza='\nComo posso ajudar?\n~> '





def menu():
    while True:
        try:
            frase=raw_input(mensagem_eliza)
        except NameError:
            frase=input(mensagem_eliza)
        frase=frase.lower()
        identificador.identifica(frase)

# MAIN
os.system('clear')
print(banner)
sair=None
os.system('espeak -v pt-br -g 4 -a 100 "Olá, como posso te ajudar?"')
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
