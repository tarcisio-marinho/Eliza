#!/bin/bash/env python
# coding=UTF-8
# by Tarcisio marinho
# github.com/tarcisio-marinho

import requests
import json
import sys
import os
import speech_recognition as sr
from datetime import datetime
from datetime import date
import random
from modulos.identificador import *
from modulos.reconhecimento import *

# CORES #
BLUE, RED, WHITE, YELLOW, MAGENTA, GREEN, END = '\33[94m', '\033[91m', '\33[97m', '\33[93m', '\033[1;35m', '\033[1;32m', '\033[0m'

banner='''{0}
 _____  _  _
|  ___|| |(_)
| |__  | | _  ____ __ _
|  __| | || ||_  // _` |
| |___ | || | / /| (_| |
\____/ |_||_|/___|\__,_|


{1}Bem vindo a Eliza, uma assistente pessoal. \nPosso te auxiliar nas suas tarefas
Digite ajuda para ver o que eu faço!
'''.format(BLUE,GREEN)

mensagem_eliza='\n{0}Como posso te ajudar?\n~$ {1}'.format(YELLOW,WHITE)

diretorio_atual=os.getcwd()



def menu():
    try:
        inicio=1
        lista=[]
        if(inicio==1):
            try:
                arquivo=open('config/inicio.txt','r')
                resp=arquivo.readline()
            except:
                os.mkdir('config')
                arquivo=open('config/inicio.txt','w')
                arquivo=open('config/inicio.txt','a')
                print('checando todas as dependências\n')
                os.system('./compilar.sh')
                arquivo.write('atualizado')
                os.system('clear')
            arquivo.close()
            inicio=0



        internet_off=False
        while True:
            os.chdir(diretorio_atual)
            if(internet_off==False):
                try:
                    print(mensagem_eliza)
                    frase=reconhecer()
                    frase=frase.lower()
                    print(frase)
                except sr.RequestError:
                    internet_off=True
                    print('Sem conexão com a internet')
                    print('Se você se conectar a internet, saia e entre denovo para falar comigo')
                    frase=raw_input(mensagem_eliza)
                except sr.UnknownValueError:
                    frase=reconhecer()
                    frase=frase.lower()
                    print(frase)
                except sr.UnknownValueError:
                    frase=reconhecer()
                    frase=frase.lower()
                    print(frase)
                except:
                    print('Erro desconhecido ocorreu')
                    internet_off=True
            else:
                pass    
            frase=raw_input(mensagem_eliza)

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
