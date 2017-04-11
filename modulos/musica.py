#!/bin/bash/env python
# coding=UTF-8
# by Tarcisio marinho
# github.com/tarcisio-marinho
import os
def musica():
    dicionario={}
    retorno=''
    i=0
    try:
        arquivo_config=open('.config.txt','r')
        retorno=arquivo_config.readline()

    except IOError:
        arquivo_config=open('.config.txt','w')

    if(retorno==''):
        pasta=raw_input('Onde está salvo suas músicas?\nEx: -> Desktop/Musicas/ ou /Musicas/ ou /Music/\n~$ ')
        caminho=os.environ['HOME'] +'/'+ pasta+'/'
        resp=os.path.isdir(caminho)
        if(resp==True): # existe
            #arquivo_config=open('.config.txt','a')
            #arquivo_config.write(caminho)
            print('Existe')
            os.chdir(caminho)
            arquivos=os.listdir(os.getcwd())
            tam=len(arquivos)
            while(i<tam):
                dicionario[i]=arquivos[i]
                if(os.path.isfile(arquivos[i])):
                    print(i,'File->', dicionario[i])
                elif(os.path.isdir(arquivos[i])):
                    print(i,'Dir ->', dicionario[i])
                i=i+1

            escolha=raw_input('Escolha: ')
            escolha=int(escolha)
            while(escolha<0 or escolha>len(dicionario)-1 or type(escolha)=='str'): # SE DIGITAR STRING ELE BUGA
                print('Numero fora da lista')
                escolha=input('Escolha: ')
                escolha=int(escolha)
            print(dicionario[escolha])
            if(os.path.isfile(dicionario[escolha])):
                print('arquivo')
            elif(os.path.isdir(dicionario[escolha])):
                print('diretorio')

        else:
            print('Não existe')

    else:
        print('eXiste')

musica()
