#!/bin/bash/env python
# coding=UTF-8
# by Tarcisio marinho
# github.com/tarcisio-marinho
import os
import re
import random
import subprocess
from list_music import *
'''
    Método que toca músicas que estão salvas em uma pasta no pc
'''
def tocar(nome=None):
    dicionario = {} # cria um dicionario para salvar as pastas e musicas digitadas pelo usuario
    tocar = [] # cria uma lista onde vai salvar as músicas encontradas e que serão tocadas
    retorno = ''
    i = 0
    try:
        arquivo_config = open('config/music.txt','r') # tenta ler o arquivo para ver se já foi escolhido o diretorio
        retorno = arquivo_config.readline()

    except IOError:
        arquivo_config = open('config/music.txt','w') # nao conseguiu ler -> cria arquivo vazio onde será as pastas das musicas

    # se o usuario digitar uma musica específica
    if(nome != None):
        if(retorno == ''):
            print('Configure primeiro o caminho de músicas')
            os.system('sleep 2')
            caminho = subprocess.check_output('zenity --title="Escolha a pasta de musicas" --file-selection --directory', shell=True)
            caminho = caminho.replace('\n','')
            arquivo_config = open('config/music.txt','a')
            arquivo_config.write(caminho)
            os.system('clear')
            print('Configurado\nExecute o comando novamente para reproduzir música escolhida\n')
            return

        else:
            achou = 0
            # retorna todas as musicas na pasta
            todas_as_musicas = listar(retorno)
            for musica in todas_as_musicas:
                padrao = re.search(nome,musica.lower())
                if(padrao != None):
                    tocar.append(musica.replace(" ", "\ ").replace(" (", " \("). replace(")", "\)"))
                    achou +=1
            if(achou == 0):
                print('Nenhuma música encontrada')

            elif(achou == 1):
                print('Música encontrada\nReproduzindo...')
                os.system('sleep 2')
                try:
                    subprocess.check_output('xdg-open '+tocar[0], shell=True)
                except:
                    print('Erros ')

                os.system('sleep 2')
                os.system('clear')

            elif(achou > 1):
                print('Várias músicas encontradas\nVou escolher uma aleatória, espero que goste :)\n')
                tam = len(tocar)
                os.system('sleep 2')
                x = random.randrange(0,tam)
                try:
                    print('tocando: '+tocar[x]+'\n\n')
                    subprocess.check_output('xdg-open '+tocar[x], shell=True)
                except:
                    print('Erros')
                os.system('sleep 2')
                os.system('clear')



    # senão escolhe a música para tocar
    elif(retorno == ''):
        print('Escolha o caminho da sua pasta de músicas')
        os.system('sleep 2')
        os.system('clear')
        caminho = subprocess.check_output('zenity --title="Escolha a pasta de musicas" --file-selection --directory', shell=True)
        caminho = caminho.replace('\n','')
        resp = os.path.isdir(caminho) # checa se o diretorio existe

        if(resp == True): # existe

        # abre o arquivo .config.txt para salvar o local das musicas
        # e percorre todos os arquivos dentro do diretorio e salva no dicionario
        # escolhe a musica dentro do dicionario

            arquivo_config = open('config/music.txt','a')
            print('Existe')
            os.chdir(caminho)
            arquivos = os.listdir(os.getcwd())
            tam = len(arquivos)

            while(i < tam):
                dicionario[i] = arquivos[i]
                if(os.path.isfile(arquivos[i])):
                    print(i,'File->', dicionario[i])
                elif(os.path.isdir(arquivos[i])):
                    print(i,'Dir ->', dicionario[i])
                i+=1

            while True: # valida que o usuario não digite letras
                try:
                    escolha = int(raw_input('Escolha: '))
                    break
                except KeyboardInterrupt:
                    return
                except:
                    print('Apenas números\n')

            while(escolha < 0 or escolha > len(dicionario)-1):
                print('Numero fora da lista')
                while True: # valida que o usuario não digite letras
                    try:
                        escolha = int(raw_input('Escolha: '))
                        break
                    except KeyboardInterrupt:
                        return
                    except:
                        print('Apenas números\n')

                        os.system('sleep 2')
            os.system('clear')

            if(os.path.isfile(dicionario[escolha])): # arquivo - tocar musica
                musica = dicionario[escolha].replace(" ", "\ ").replace(" (", " \("). replace(")", "\)")
                subprocess.check_output('xdg-open '+musica, shell=True)
                arquivo_config.write(caminho)
                arquivo_config.close()
                os.system('sleep 2')
                os.system('clear')

            elif(os.path.isdir(dicionario[escolha])): # diretorio - escolher musica primeiro para depois tocar
                dicionario2 = {}
                os.chdir(os.getcwd()+'/'+dicionario[escolha])
                musicas = os.listdir(os.getcwd())
                tam = len(musicas)
                i = 0

                while(i < tam):
                    dicionario2[i] = musicas[i]

                    if(os.path.isfile(musicas[i])):
                        print(i,'File->', dicionario2[i])

                    elif(os.path.isdir(musicas[i])):
                        print(i,'Dir ->', dicionario2[i])
                    i=i+1

                while True: # valida que o usuario não digite letras
                    try:
                        escolha = int(raw_input('Escolha: '))
                        break
                    except KeyboardInterrupt:
                        return
                    except:
                        print('Apenas números\n')

                while(escolha < 0 or escolha > len(dicionario2)-1): # SE DIGITAR STRING ELE BUGA
                    print('Numero fora da lista')
                    while True: # valida que o usuario não digite letras
                        try:
                            escolha=int(raw_input('Escolha: '))
                            break
                        except KeyboardInterrupt:
                            return
                        except:
                            print('Apenas números\n')

                print(dicionario2[escolha])
                musica = dicionario2[escolha].replace(" ", "\ ").replace(" (", " \("). replace(")", "\)")
                subprocess.check_output('xdg-open '+musica, shell=True)
                arquivo_config.write(caminho)
                arquivo_config.close()
                os.system('sleep 2')
                os.system('clear')



        else:
            print('Diretório não existe')

    # ja esta salvo no arquivo .config.txt, e ele so escolhe a musica
    else:
        arquivo_config = open('config/music.txt','r')
        caminho = arquivo_config.readline()
        os.chdir(caminho)
        arquivos = os.listdir(os.getcwd())
        tam = len(arquivos)

        while(i < tam):
            dicionario[i] = arquivos[i]
            if(os.path.isfile(arquivos[i])):
                print(i,'File->', dicionario[i])
            elif(os.path.isdir(arquivos[i])):
                print(i,'Dir ->', dicionario[i])
            i+=1

        while True: # valida que o usuario não digite letras
            try:
                escolha = int(raw_input('Escolha: '))
                break
            except KeyboardInterrupt:
                return
            except:
                print('Apenas números\n')


        while(escolha < 0 or escolha > len(dicionario)-1): # SE DIGITAR STRING ELE BUGA
            print('Numero fora da lista')
            while True: # valida que o usuario não digite letras
                try:
                    escolha = int(raw_input('Escolha: '))
                    break
                except KeyboardInterrupt:
                    return
                except:
                    print('Apenas números\n')

                    os.system('sleep 2')
        os.system('clear')

        if(os.path.isfile(dicionario[escolha])): # arquivo - tocar musica
            musica = dicionario[escolha].replace(" ", "\ ").replace(" (", " \("). replace(")", "\)")
            subprocess.check_output('xdg-open '+musica, shell=True)
            os.system('sleep 2')
            os.system('clear')

        elif(os.path.isdir(dicionario[escolha])): # diretorio - escolher musica primeiro para depois tocar
            dicionario2 = {}
            os.chdir(os.getcwd()+'/'+dicionario[escolha])
            musicas = os.listdir(os.getcwd())
            tam = len(musicas)
            i=0

            while(i < tam):
                dicionario2[i]=musicas[i]
                if(os.path.isfile(musicas[i])):
                    print(i,'File->', dicionario2[i])
                elif(os.path.isdir(musicas[i])):
                    print(i,'Dir ->', dicionario2[i])
                i+=1

            while True: # valida que o usuario não digite letras
                try:
                    escolha = int(raw_input('Escolha: '))
                    break
                except KeyboardInterrupt:
                    return
                except:
                    print('Apenas números\n')


            while(escolha < 0 or escolha > len(dicionario2)-1): # SE DIGITAR STRING ELE BUGA
                print('Numero fora da lista')
                while True: # valida que o usuario não digite letras
                    try:
                        escolha = int(raw_input('Escolha: '))
                        break
                    except KeyboardInterrupt:
                        return
                    except:
                        print('Apenas números\n')


            print(dicionario2[escolha])
            musica = dicionario2[escolha].replace(" ", "\ ").replace(" (", " \("). replace(")", "\)")
            subprocess.check_output('xdg-open '+musica, shell=True)
            os.system('sleep 2')
            os.system('clear')
