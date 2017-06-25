#!/bin/bash/env python
# coding=UTF-8
# by Tarcisio marinho
# github.com/tarcisio-marinho




def ajudar(comando,lista_de_comandos):
    encontrou=0
    for com in lista_de_comandos:
        if(comando==com):
            if(com == u'busca'):
                print('O comando busca, procura no wikipedia o que você quiser\nEx: busca barack obama\n')

            elif(com == u'email'):
                print('O comando email, manda emails para o email digitado assim que chegar alguma atualização sua\nApenas digite o email para cadastrar')

            elif(com == u'quem é'):
                print('O comando quem é, busca no wikipedia sobre uma pessoa\nEx: quem é barack obama')

            elif(com == u'hora'):
                print('O comando hora, mostra a hora atual\nNão precisa de nenhum argumento')

            elif(com == u'dia'):
                print('O comando dia, mostra o dia atual\nNão precisa de nenhum argumento')

            elif(com == u'renomear'):
                print('O comando renomear, recebe como parâmetro um arquivo ou uma pasta que deseja ser renomeada\nOs arquivos a serem renomeados estão dentro da pasta de arquivos que você já salvou\nE as pastas estão no diretório do projeto')

            elif(com == u'ip'):
                print('O comando IP, Mostra o seu IP externo, se você estiver conectado na internet\nNão precisa de nenhum argumento')

            elif(com == u'onde estou'):
                print('O comando onde estou, mostra onde você está localizado, se você tiver internet\nNão preicsa de nenhum argumento extra')

            elif(com == u'pais'):
                print('O comando pais, mostra qual o país que você esta localizado\nNão precisa de nenhum argumento')

            elif(com == u'tocar'):
                print('O comando tocar pode tocar uma música informada ou escolher uma música\nPrimeira vez use o tocar sem argumentos: tocar.\nPara assim configurar o diretório de músicas.\nVocê pode executar o tocar sozinho, para escolher a pasta e a música\nVocê também pode executar o tocar e nome de música que você quer.\nEx: tocar almost easy\n')

            elif(com == u'localizacao'):
                print('O comando localizacao, localiza onde você está\nNão precisa de argumento extra')

            elif(com == u'cotacao'):
                print('O comando cotacao, mostra a cotação atual da moeda informada\nEx: cotacao dolar\n')

            elif(com == u'criar'):
                print('O comando criar, cria um arquivo vazio ou um diretorio\nOs arquivos são salvos na pasta arquivos, que está dentro do diretório do projeto\nEx: criar arquivo Compromissos\nEx2: criar diretorio fotos\n')

            elif(com == u'remover'):
                print('O comando remover, remove um arquivo ou diretório\nPara remover arquivos, o arquivo tem que estar salvo na pasta arquivos\nEx: remover arquivo Compromissos')

            elif(com == u'editar'):
                print('O comando editar, Edita um arquivo com o seu editor de texto preferido\nEx: editar arquivo Compromissos\n')

            elif(com == u'calculadora'):
                print('O comando calculadora, abre uma calculadora\nNão precisa de argumento extras\n')

            elif(com == u'esvaziar'):
                print('O comando esvaziar, esvazia a sua lixeira\nNão precisa de argumento extra\n')

            elif(com == u'sair'):
                print('O comando sair, sai do Eliza\n')

            elif(com == u'onde fica'):
                print('O comando onde fica, procura a cidade, país ou estado desejado\nEx: onde fica pernambuco\n')

            elif(com == u'procurar'):
                print('O comando procurar, procura o filme digitado\nEx: procurar filme matrix\n')

            elif(com == u'clima'):
                print('O comando clima, mostra a temperatura e a condição temporal da cidade\nEx: clima recife\n')

            elif(com == u'ajuda'):
                print('O comando ajuda, mostra sobre os comandos existentes\nEx: ajuda editar')

            elif(com == u'clear'):
                print('O comando clear, limpa a tela, quando ela tiver muito cheia\nNão precisa de outros argumentos\n')

            elif(com == u'historico'):
                print('O comando historico, mostra o historico digitado por você\nNão precisa de outros argumentos\n')

            encontrou=1

    if(encontrou==0):
        print('Os comandos existentes são: ')
        for com in lista_de_comandos:
            print(com)
        print('Para saber mais sobre um comando, digite ajuda e o nome do comando\nEx: ajuda editar\n')
