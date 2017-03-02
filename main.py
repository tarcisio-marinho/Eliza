#!/bin/usr/env python
# coding=UTF-8
# Eliza chatbot
# by Tarcísio Marinho
# github.com/tarcisio-marinho



# Programa principal que executa eliza


# frase.lower()

#frase='ola eliza tudo bem'
#x=frase.split(' ') x é uma lista das palavras da frase


import os
import random
import sys
from identificador import Identificador


# cria a instância eliza que identifica a pergunta
# e a área de interesse das perguntas

eliza=Identificador()

banner='''
Bem vindo a Eliza
Iniciando Eliza ...
'''

print(banner)

#os.system('sleep 2')
print('Diga olá para eliza!')

while True:
    frase=raw_input('Você: ')
    eliza.identifica(frase)
	#frase=eliza.pergunta()
	#identificador
	#eliza.resposta(frase)
	#checa qual e a maior area de enteresse
	#perguntas_eliza.humor()
