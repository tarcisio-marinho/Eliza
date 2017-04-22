#!/bin/bash/env python
# coding=UTF-8
# by Tarcisio marinho
# github.com/tarcisio-marinho




def ajudar(comando,lista_de_comandos):
    encontrou=0
    for com in lista_de_comandos:
        if(comando==com):
            if(com=='hora'):
                print('O comando hora, mostra a hora atual\nNão precisa de nenhum argumento')

            elif(com=='dia'):
                print('O comando dia, mostra o dia atual\nNão precisa de nenhum argumento')

            elif(com=='renomear'):
                print('O comando renomear, recebe como parâmetro um arquivo ou uma pasta que deseja ser renomeada\nOs arquivos a serem renomeados estão dentro da pasta de arquivos que você já salvou\nE as pastas estão no diretório do projeto')

            elif(com=='ip'):
                print('O comando IP, Mostra o seu IP externo, se você estiver conectado na internet\nNão precisa de nenhum argumento')

            elif(com=='onde estou'):
                print('O comando onde estou, mostra onde você está localizado, se você tiver internet\nNão preicsa de nenhum argumento extra')

            elif(com=='pais'):
                print('O comando pais, mostra qual o país que você esta localizado\nNão precisa de nenhum argumento')

            elif(com=='tocar'):
                print('O comando tocar, toca uma música com seu reprodutor de música favorito\nSe você nunca tiver usado ele, primeiramente ele pede para você escolher o diretorio onde suas músicas estão salvas\nEle entra no diretorio e lista as músicas e pastas, Você escolhe qual música vai querer\nDepois de executar a música, se quiser escolher denovo, não precisa mais informar o caminho de músicas\nSe ele salvou o caminho errado, entre na pasta do projeto, pressione CTRL + H e exclua o arquivo .config.txt\n')

            elif(com=='localizacao'):
                print('O comando localizacao, localiza onde você está\nNão precisa de argumento extra')

            elif(com=='cotacao'):
                print('O comando cotacao, mostra a cotação atual da moeda informada\nEx: cotacao dolar\n')

            elif(com=='criar'):
                print('O comando criar, cria um arquivo vazio ou um diretorio\nOs arquivos são salvos na pasta arquivos, que está dentro do diretório do projeto\nEx: criar arquivo Compromissos\nEx2: criar diretorio fotos\n')

            elif(com=='remover'):
                print('O comando remover, remove um arquivo ou diretório\nPara remover arquivos, o arquivo tem que estar salvo na pasta arquivos\nEx: remover arquivo Compromissos')

            elif(com=='editar'):
                print('O comando editar, Edita um arquivo com o seu editor de texto preferido\nEx: editar arquivo Compromissos\n')

            elif(com=='calculadora'):
                print('O comando calculadora, abre uma calculadora\nNão precisa de argumento extras\n')

            elif(com=='esvaziar'):
                print('O comando esvaziar, esvazia a sua lixeira\nNão precisa de argumento extra\n')

            elif(com=='sair'):
                print('O comando sair, sai do Eliza\n')

            elif(com=='onde fica'):
                print('O comando onde fica, procura a cidade, país ou estado desejado\nEx: onde fica pernambuco\n')

            elif(com=='procurar'):
                print('O comando procurar, procura o filme digitado\nEx: procurar filme matrix\n')

            elif(com=='clima'):
                print('O comando clima, mostra a temperatura e a condição temporal da cidade\nEx: clima recife\n')

            elif(com=='ajuda'):
                print('O comando ajuda, mostra sobre os comandos existentes\nEx: ajuda editar')

            elif(com=='clear'):
                print('O comando clear, limpa a tela, quando ela tiver muito cheia\nNão precisa de outros argumentos\n')

            elif(com=='historico'):
                print('O comando historico, mostra o historico digitado por você\nNão precisa de outros argumentos\n')
                
            encontrou=1

    if(encontrou==0):
        print('Os comandos existentes são: ')
        for com in lista_de_comandos:
            print(com)
        print('Para saber mais sobre um comando, digite ajuda e o nome do comando\nEx: ajuda editar\n')
