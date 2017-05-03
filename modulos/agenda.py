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
pasta='arquivos'

def Agenda(nome_arquivo):
    try: # tenta criar pasta
        os.mkdir(pasta)
        os.chdir(os.getcwd()+'/'+'arquivos')
    except OSError: # pasta ja existe
        os.chdir(os.getcwd()+'/'+'arquivos')

    if(nome_arquivo!=None):
        arquivo_novo=open(nome_arquivo,'w')
        arquivo_novo=open(nome_arquivo,'a')
        try:
            while True:
                frase=raw_input()
                arquivo_novo.write(frase+'\n')
        except KeyboardInterrupt:
            print('arquivo foi salvo na pasta arquivos')
            os.system('espeak -v pt-br -g 4 -a 100 "arquivo foi salvo na pasta arquivos"')
        arquivo_novo.close()

    else:
        arquivo=open('agenda.txt','a')
        try:
            while True:
                frase=raw_input()
                arquivo.write(frase+'\n')
        except KeyboardInterrupt:
            print('Arquivo salvo como agenda.txt na pasta agendados')
            os.system('espeak -v pt-br -g 4 -a 100 "arquivo salvo como agenda.txt na pasta agendados"')
        arquivo.close()
