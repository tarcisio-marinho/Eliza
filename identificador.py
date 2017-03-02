#!/bin/usr/env python
# coding=UTF-8
# Eliza chatbot
# by Tarcisio Marinho
# github.com/tarcisio-marinho


# Classe que identifica qual o tipo de pergunta

import random
from inicio_conversa import Inicio
from sobre_eliza import Para_eliza

class Identificador():
    def __init__(self): # cria os atributos das areas de interesse
        self.esportes=0
        self.sentimentos=0
        self.sentido_da_vida=0
        self.pergunta=False

    def identifica(self,frase): # metodo que identifica a pergunta
        palavras=frase.split(' ') # divide a frase em palavras

        # IDENTIFICA SE É UMA PERGUNTA
        x=len(palavras)-1
        y=len(palavras[x])
        j=palavras[x]
        k=len(j)
        i=j[k-1]
        if(palavras[x]=='?' or i=='?'):
        #significa que eh uma pergunta
            self.pergunta=True
            print(self.pergunta)


        if(len(palavras)<3): # inicio de conversa
            objeto=Inicio() # cria o objeto
            objeto.compara(palavras) # metodo que compara as palavras
