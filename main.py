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

# CORES #
BLUE, RED, WHITE, YELLOW, MAGENTA, GREEN, END = '\33[94m', '\033[91m', '\33[97m', '\33[93m', '\033[1;35m', '\033[1;32m', '\033[0m'

banner='''{0}
 _____  _  _
|  ___|| |(_)
| |__  | | _  ____ __ _
|  __| | || ||_  // _` |
| |___ | || | / /| (_| |
\____/ |_||_|/___|\__,_|            


{1}Bem vindo a Eliza, sua assistente pessoal
Digite ajuda para ver a documentação
'''.format(BLUE,GREEN)

mensagem_eliza='\n{0}Como posso te ajudar?\n~$ {1}'.format(YELLOW,WHITE)

diretorio_atual=os.getcwd()



def menu():
    try:
        inicio=1
        lista=[]
        if(inicio==1):
            try:
                arquivo=open('.inicio.txt','r')
                resp=arquivo.readline()
            except:
                arquivo=open('.inicio.txt','w')
                arquivo=open('.inicio.txt','a')
                print('checando todas as dependências\n')
                os.system('./compilar.sh')
                arquivo.write('atualizado')
                os.system('clear')
            arquivo.close()
            inicio=0




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
    except KeyboardInterrupt:
        while True:
            try:
                sair=raw_input('Deseja sair? ')
                if(sair=='sim' or sair=='1' or sair=='quit' or sair=='s' or sair=='exit'):
                    print('Saindo...')
                    exit()
                else:
                    menu()
            except KeyboardInterrupt:
                sair=raw_input('Sim ou não?')
                if(sair=='sim' or sair=='1' or sair=='quit' or sair=='s' or sair=='exit'):
                    print('Saindo...')
                    exit()
                else:
                    menu()

# MAIN #
if __name__=="__main__":
    os.system('clear')
    print(banner)
    menu()
