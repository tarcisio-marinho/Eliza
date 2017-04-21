#!/bin/bash/env python
# coding=UTF-8
# by Tarcisio marinho
# github.com/tarcisio-marinho
import os
def tocar():
    dicionario={} # cria um dicionario para salvar as pastas e musicas digitadas pelo usuario
    retorno=''
    i=0
    try:
        arquivo_config=open('.config.txt','r') # tenta ler o arquivo para ver se já foi escolhido o diretorio
        retorno=arquivo_config.readline()

    except IOError:
        arquivo_config=open('.config.txt','w') # nao conseguiu ler -> cria arquivo vazio onde será as pastas das musicas

    if(retorno==''):
        pasta=raw_input('Onde está salvo suas músicas?\nEx: -> Desktop/Musicas/ ou /Musicas/ ou /Music/\n~$ ')
        caminho=os.environ['HOME'] +'/'+ pasta+'/'
        resp=os.path.isdir(caminho) # checa se o diretorio existe

        if(resp==True): # existe

        # abre o arquivo .config.txt para salvar o local das musicas
        # e percorre todos os arquivos dentro do diretorio e salva no dicionario
        # escolhe a musica dentro do dicionario

            arquivo_config=open('.config.txt','a')
            arquivo_config.write(caminho)
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

            while(escolha<0 or escolha>len(dicionario)-1): # SE DIGITAR STRING ELE BUGA
                print('Numero fora da lista')
                escolha=input('Escolha: ')
                escolha=int(escolha)
            os.system('clear')

            if(os.path.isfile(dicionario[escolha])): # arquivo - tocar musica
                musica=dicionario[escolha].replace(" ", "\ ").replace(" (", " \("). replace(")", "\)")
                os.system('xdg-open '+musica)
                os.system('sleep 1')

            elif(os.path.isdir(dicionario[escolha])): # diretorio - escolher musica primeiro para depois tocar
                dicionario2={}
                os.chdir(os.getcwd()+'/'+dicionario[escolha])
                musicas=os.listdir(os.getcwd())
                tam=len(musicas)
                i=0

                while(i<tam):
                    dicionario2[i]=musicas[i]

                    if(os.path.isfile(musicas[i])):
                        print(i,'File->', dicionario2[i])

                    elif(os.path.isdir(musicas[i])):
                        print(i,'Dir ->', dicionario2[i])
                    i=i+1

                escolha=raw_input('Escolha: ')
                escolha=int(escolha)

                while(escolha<0 or escolha>len(dicionario2)-1): # SE DIGITAR STRING ELE BUGA
                    print('Numero fora da lista')
                    escolha=input('Escolha: ')
                    escolha=int(escolha)
                print(dicionario2[escolha])
                musica=dicionario2[escolha].replace(" ", "\ ").replace(" (", " \("). replace(")", "\)")
                os.system('xdg-open '+musica)
                os.system('sleep 1')



        else:
            print('Diretório não existe')

    else: # ja esta salvo no arquivo .config.txt, e ele so escolhe a musica
        arquivo_config=open('.config.txt','r')
        caminho=arquivo_config.readline()
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

        while(escolha<0 or escolha>len(dicionario)-1): # SE DIGITAR STRING ELE BUGA
            print('Numero fora da lista')
            escolha=input('Escolha: ')
            escolha=int(escolha)
        os.system('clear')

        if(os.path.isfile(dicionario[escolha])): # arquivo - tocar musica
            musica=dicionario[escolha].replace(" ", "\ ").replace(" (", " \("). replace(")", "\)")
            os.system('xdg-open '+musica)
            os.system('sleep 1')

        elif(os.path.isdir(dicionario[escolha])): # diretorio - escolher musica primeiro para depois tocar
            dicionario2={}
            os.chdir(os.getcwd()+'/'+dicionario[escolha])
            musicas=os.listdir(os.getcwd())
            tam=len(musicas)
            i=0

            while(i<tam):
                dicionario2[i]=musicas[i]
                if(os.path.isfile(musicas[i])):
                    print(i,'File->', dicionario2[i])
                elif(os.path.isdir(musicas[i])):
                    print(i,'Dir ->', dicionario2[i])
                i=i+1

            escolha=raw_input('Escolha: ')
            escolha=int(escolha)

            while(escolha<0 or escolha>len(dicionario2)-1): # SE DIGITAR STRING ELE BUGA
                print('Numero fora da lista')
                escolha=input('Escolha: ')
                escolha=int(escolha)

            print(dicionario2[escolha])
            musica=dicionario2[escolha].replace(" ", "\ ").replace(" (", " \("). replace(")", "\)")
            os.system('xdg-open '+musica)
            os.system('sleep 1')
