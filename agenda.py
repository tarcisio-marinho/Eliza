#!/bin/bash/env python
# coding=UTF-8
# by Tarcisio marinho
# github.com/tarcisio-marinho
import os

# criar pasta para salvar os arquivos do agendar
#try:
# os.mkdir('agenda')
#except:
# ja tem entao
# os.entrarpasta('agenda')

def Agenda(nome_arquivo):
    if(nome_arquivo!=None):
        arquivo_novo=open(nome_arquivo,'w')
        arquivo_novo=open(nome_arquivo,'a')
        try:
            while True:
                frase=raw_input()
                arquivo_novo.write(frase+'\n')
        except KeyboardInterrupt:
            os.system('espeak -v pt-br -g 4 -a 100 "arquivo foi salvo"')

    else:
        arquivo=open('agenda.txt','a')
        try:
            while True:
                frase=raw_input()
                arquivo.write(frase+'\n')
        except KeyboardInterrupt:
            print('Arquivo salvo como agenda.txt')
            os.system('espeak -v pt-br -g 4 -a 100 "arquivo salvo como agenda.txt"')
