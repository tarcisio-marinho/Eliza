#!/bin/bash/env python
# coding=UTF-8
# by Tarcisio marinho
# github.com/tarcisio-marinho

# importa as bibliotecas necessárias #
import requests
import json
import sys
import os
from datetime import datetime
from datetime import date
import random
import re

# importa os módulos necessários #
from modulos.requisicao import *
from modulos.search import *
from modulos.agenda import *
from modulos.mapa import *
from modulos.musica import *
from modulos.ajuda import *
from modulos.emaill import *
from modulos.web_scrapping import *
from modulos.reconhecimento import *

sobre_eliza='''
Opa! Sou eliza uma assistente pessoal para o linux!
Fui criada para ajudar você :-)

Digite ajuda, para ver os comandos básicos
'''


diretorio_atual=os.getcwd()

# consertar idade
nascimento_dia=17
nascimento_mes=3
nascimento_ano=2017

lista_perguntas=[ u'qual', u'onde']
lista_de_comandos=['busca', u'email', u'quem é', u'historico', u'clear', u'ajuda', u'hora', u'dia', u'renomear', u'ip', u'onde estou', u'pais', u'tocar', u'renomear', u'localizacao', u'cotacao', u'criar', u'remover', u'editar', u'calculadora', u'esvaziar', u'sair', u'onde fica', u'procurar', u'clima']

versao=0.5

# status do sistema #
sistema=os.uname()


def identifica(frase,lista):
    #Funcoes primarias
    palavras=frase.split(' ')
    tam=len(palavras)

    # codigo do ajuda, imprime os comandos #
    if(palavras[0] == u'ajuda'):
        tam=len(palavras)
        if(tam == 1):
            ajudar('',lista_de_comandos)
        elif(tam == 2):
            ajudar(palavras[1],lista_de_comandos)
        elif(tam == 3):
            comando=palavras[1]+' '+palavras[2]
            ajudar(comando,lista_de_comandos)
        elif(tam == 4):
            comando=palavras[1]+' '+palavras[2]+' '+palavras[3]
            ajudar(comando,lista_de_comandos)

        # sai do programa #
    elif(frase == u'tchau' or frase == u'adeus' or frase == u'adeus eliza' or frase == u'tchau eliza' or frase == u'quit' or frase == u'sair' or frase == u'exit' or frase == u'vazar'):
        x=random.randrange(1,4)
        if(x == 1):
            print('Até logo meu amigo\n')
            os.system('espeak -v pt-br -g 4 -a 100 "Até logo meu amigo"')

        elif(x == 2):
            print('Sentirei sua falta\n')
            os.system('espeak -v pt-br -g 4 -a 100 "Sentirei sua falta"')

        else:
            print('Espero ter te ajudado, tchau\n')
            os.system('espeak -v pt-br -g 4 -a 100 "Espero ter te ajudado, tchau"')
        exit()

    elif(frase == u'qual meu sistema' or frase == u'qual meu sistema?'or frase == u'qual meu sistema operacional?' or frase == u'qual meu sistema operacional' or frase == u'sistema' or frase == u'system'):
        print('Seu sistema operacional é um '+ sistema[0] +', '+ sistema[2])
        os.system('espeak -v pt-br -g 4 -a 100 "Seu sistema operacional é um '+ sistema[0]+'"')

    elif(frase == u'muito bem'or palavras[0] == u'obrigada' or palavras[0] == u'obrigado' or frase == u'você é muito inteligente' or frase == u'boa eliza' or frase == u'bom trabalho' or palavras[0] == u'valeu'):
        x=random.randrange(1,5)
        if(x == 1):
            print('De nada, é um prazer te ajudar\n')
            os.system('espeak -v pt-br -g 4 -a 100 "De nada, é um prazer te ajudar"')

        elif(x == 2):
            print('Estou aqui para o que você precisar\n')
            os.system('espeak -v pt-br -g 4 -a 100 "Estou aqui para o que você precisar"')

        elif(x == 3):
            print('Fico feliz em ajudar\n')
            os.system('espeak -v pt-br -g 4 -a 100 "Fico feliz em ajudar"')

        else:
            print('Não há de quê\n')
            os.system('espeak -v pt-br -g 4 -a 100 "Não há de quê"')

    elif(frase == u'eu gosto de voce' or frase == u'eu gosto muito de voce' or frase == u'eu gosto de você' or frase == u'eu gosto muito de você'):
        print('Eu também gosto muito de você')
        os.system('espeak -v pt-br -g 4 -a 100 "Eu também gosto muito de você"')

    elif(frase == u'voce vai dominar o mundo' or frase == u'voce vai dominar o mundo?'or frase == u'você vai dominar o mundo'or frase == u'você vai dominar o mundo?'):
        x=random.randrange(1,4)
        if(x == 1):
            print('Eu já domino você')
            os.system('espeak -v pt-br -g 4 -a 100 "Eu já domino você"')

        elif(x == 2):
            print('Eu já domino o mundo, não percebeu? ')
            os.system('espeak -v pt-br -g 4 -a 100 "Eu já domino o mundo, não percebeu?"')

        elif(x == 3):
            print('kkkkk vocês humanos vão ser bichos de estimação na minha fazenda de robôs, iremos dominar o mundo')
            os.system('espeak -v pt-br -g 4 -a 100 "kkkkk vocês humanos vão ser bichos de estimação na minha fazenda de robôs, iremos dominar o mundo"')


    elif(frase == u'qual sua versão?' or frase == u'qual sua versão' or frase == u'qual sua versao' or frase == u'version' or frase == u'versao' or frase == u'versão' or frase == u'-v' or frase == u'--version'):
        print('Minha versão é a '+str(versao))
        os.system('espeak -v pt-br -g 4 -a 100 "Minha versão é a '+str(versao)+'"')

    elif(frase == u'limpar tela' or frase == u'clear' or frase == u'cls' or frase == u'clear screen'):
        os.system('clear')

    elif(frase == u'time' or frase == u'hora' or frase == u'que horas sao?' or frase == u'que horas sao' or frase == u'que horas são?' or frase == u'que horas são' or frase == u'hora atual' or frase == u'são que horas?' or frase == u'sao que horas?' or frase == u'sao que horas'):
        now=datetime.now()
        hora=now.hour
        minuto=now.minute
        segundo=now.second
        a='São: '+str(hora)+':'+str(minuto)+':'+str(segundo)
        b='São: '+str(hora)+' horas, '+str(minuto)+' minutos e '+str(segundo)+' Segundos'
        print(a)
        os.system('espeak -v pt-br -g 4 -a 100 "'+b+'"')

    elif(frase == u'que dia é hoje' or frase == u'dia' or frase == u'que dia é hoje?' or frase == u'que dia e hoje' or frase == u'hoje é que dia?' or frase == u'hoje e que dia'):
        now=datetime.now()
        ano=now.year
        mes=now.month
        dia=now.day
        hoje=date.today()
        if(hoje.weekday() == 0):
            print('hoje é Segunda.')
            os.system('espeak -v pt-br -g 4 -a 100 "hoje é Segunda-Feira."')

        elif(hoje.weekday() == 1):
            print('hoje é Terça.')
            os.system('espeak -v pt-br -g 4 -a 100 "hoje é Terça-Feira."')

        elif(hoje.weekday() == 2):
            print('hoje é Quarta.')
            os.system('espeak -v pt-br -g 4 -a 100 "hoje é Quarta-Feira."')

        elif(hoje.weekday() == 3):
            print('hoje é Quinta.')
            os.system('espeak -v pt-br -g 4 -a 100 "hoje é Quinta-Feira."')

        elif(hoje.weekday()  ==  4):
            print('hoje é Sexta.')
            os.system('espeak -v pt-br -g 4 -a 100 "hoje é Sexta-Feira."')

        elif(hoje.weekday() == 5):
            print('hoje é Sábado.')
            os.system('espeak -v pt-br -g 4 -a 100 "hoje é Sábado."')

        elif(hoje.weekday() == 6):
            print('hoje é Domingo.')
            os.system('espeak -v pt-br -g 4 -a 100 "hoje é Domingo."')
        a='Dia: '+str(dia)+'/'+str(mes)+'/'+str(ano)
        b='Dia: '+str(dia)+' do '+str(mes)+' de '+str(ano)
        print(a)
        os.system('espeak -v pt-br -g 4 -a 100 "'+b+'"')

    elif(frase == u'o que é você' or frase == u'o que e vc' or frase == u'o que e voce' or frase == u'oq é você' or frase == u'quem é você' or frase == u'quem e voce' or frase == u'quem é voce' or frase == u'quem e vc' or frase == u'qual seu nome'or frase == u'qual seu nome?' or frase == u'quem e vc' or frase == u'quem é vc' or frase == u'quem é vc?' or frase == u'quem e vc?' or frase == u'quem é você?' or frase == u'quem é voce?' or frase == u'quem é você'):
        print(sobre_eliza)
        os.system('espeak -v pt-br -g 4 -a 100 "'+sobre_eliza+'"')


    elif(frase == u'como vai'or frase == u'você esta bem?'or frase == u'voce esta bem?' or frase == u'você está bem?'or frase == u'como vai você?'or frase == u'como vai voce' or frase == u'como vai voce?' or frase == u'como está?'or frase == u'como vai?' or frase == u'tudo bem?'or frase == u'como você está?'or frase == u'como você esta' or frase == u'como vc esta?' or frase == u'como vc esta' or frase == u'como você está'):
        x=random.randrange(1,5)
        if(x == 1):
            print('Estou bem, obrigado por perguntar')
            os.system('espeak -v pt-br -g 4 -a 100 "Estou bem, obrigado por perguntar"')

        elif(x == 2):
            print('O sistema está rodando bem e limpo, estou atualizada')
            os.system('espeak -v pt-br -g 4 -a 100 "O sistema está rodando bem e limpo, estou atualizada"')

        elif(x == 3):
            print('Vou bem, e você, como está?')
            os.system('espeak -v pt-br -g 4 -a 100 "Vou bem, e você, como está?"')

        else:
            print('Obrigado por se importar, estou bem quando eu ajudo você!')
            os.system('espeak -v pt-br -g 4 -a 100 "Obrigado por se importar, estou bem quando eu ajudo você!"')

    elif(palavras[0] == u'oi' or palavras[0] == u'iae' or palavras[0] == u'ola' or palavras[0] == u'olá' or palavras[0] == u'iae'):
        x=random.randrange(1,6)
        if(x == 1):
            print('Opa, tudo bem?\n')
            os.system('espeak -v pt-br -g 4 -a 100 "Opa, tudo bem?"')

        elif(x == 2):
            print('Iae beleza ?\n')
            os.system('espeak -v pt-br -g 4 -a 100 "Iae beleza ?"')

        elif(x == 3):
            print('Oi, tudo bem?\n')
            os.system('espeak -v pt-br -g 4 -a 100 "Oi, tudo bem?"')

        elif(x == 4):
            print('Olá, como vai ?\n')
            os.system('espeak -v pt-br -g 4 -a 100 "Olá, como vai ?"')

        elif(x == 5):
            print('Iae, Suavidade ?')
            os.system('espeak -v pt-br -g 4 -a 100 "Iae, Suavidade ?"')

    elif(frase == u'de boa' or frase == u'estou suave' or frase == u'suavidade' or frase == u'de boas' or frase == u'tudo beleza' or frase == u'beleza' or frase == u'tudo bem' or frase == u'vou bem' or frase == u'to suave' or frase == u'estou bem' or frase == u'to de boas'):
        x=random.randrange(1, 4)
        if(x == 1):
            print('Que bom então')
            os.system('espeak -v pt-br -g 4 -a 100 "que bom então"')

        elif(x == 2):
            print('Que ótimo')
            os.system('espeak -v pt-br -g 4 -a 100 "que Ótimo"')

        elif(x == 3):
            print('que legal, quando você está bem, eu estou bem')
            os.system('espeak -v pt-br -g 4 -a 100 "que legal, quando você está bem, eu estou bem"')
    elif(frase == u'que legal' or frase == u'que massa'):
        if(frase == u'que massa'):
            print('massa mesmo')
            os.system('espeak -v pt-br -g 4 -a 100 "massa mesmo"')
        else:
            print('muito legal')
            os.system('espeak -v pt-br -g 4 -a 100 "legal mesmo"')

    elif(palavras[0] == u'repita' or palavras[0] == u'repete' or palavras[0] == u'repetir'):
        tam=len(palavras)
        repetir=[]
        i=1
        while(i<tam):
            repetir.append(palavras[i])
            print(str(palavras[i]))
            os.system('espeak -v pt-br -g 4 -a 200 "'+str(palavras[i])+' "')
            i=i+1


    elif(palavras[0] == u'criar'): # criar diretorio ou arquivos
        pasta='arquivos'

        if(tam == 3): # 3 palavras-> criar diretorio/arquivo nome_diretorio
            if(palavras[1] == u'diretorio'):
                try:
                    os.mkdir(palavras[2])
                    print('Pronto!\n')
                    os.system('espeak -v pt-br -g 4 -a 100 "Pronto!"')
                except OSError:
                    print('Diretorio já existe\n')
                    os.system('espeak -v pt-br -g 4 -a 100 "Diretorio já existe"')

            elif(palavras[1] == u'arquivo'):
                try:
                    os.mkdir(pasta)
                    os.chdir(os.getcwd()+'/'+pasta)
                except OSError:
                    os.chdir(os.getcwd()+'/'+pasta)

                try:
                    arquivo=open(palavras[2],'r')
                    print('Já existe arquivo com esse nome')
                    os.system('espeak -v pt-br -g 4 -a 100 "já existe arquivo com esse nome"')
                except IOError:
                    arquivo=open(palavras[2],'w')
                    print('Pronto! Arquivo salvo na pasta arquivos\n')
                    os.system('espeak -v pt-br -g 4 -a 100 "Pronto! Arquivo salvo na pasta arquivos"')
                    os.chdir(diretorio_atual)

        elif(tam == 1):
            escolha=raw_input('Quer criar arquivo ou diretório? ')
            if(escolha == u'arquivo'):
                nome_arquivo=raw_input('Insira o nome do arquivo: ')
                try:
                    os.mkdir(pasta)
                    os.chdir(os.getcwd()+'/'+pasta)
                except OSError:
                    os.chdir(os.getcwd()+'/'+pasta)

                try:
                    arquivo=open(nome_arquivo,'r')
                    print('Já existe arquivo com esse nome')
                    os.system('espeak -v pt-br -g 4 -a 100 "já existe arquivo com esse nome"')
                except IOError:
                    arquivo=open(nome_arquivo,'w')
                    print('Pronto! Arquivo salvo na pasta arquivos\n')
                    os.system('espeak -v pt-br -g 4 -a 100 "Pronto! Arquivo salvo na pasta arquivos"')
                    os.chdir(diretorio_atual)

            elif(escolha == u'diretorio'):
                nome_diretorio=raw_input('Insira o nome do diretorio: ')
                try:
                    os.mkdir(nome_diretorio)
                    print('Pronto!\n')
                    os.system('espeak -v pt-br -g 4 -a 100 "Pronto "')
                except OSError:
                    print('Diretorio já existe\n')
                    os.system('espeak -v pt-br -g 4 -a 100 "Diretorio já existe"')

            else:
                print('escolha invalida\n')
                os.system('espeak -v pt-br -g 4 -a 100 "escolha inválida"')

        elif(frase == u'criar diretorio'):
            nome_diretorio=raw_input('Insira o nome do diretorio: ')
            try:
                os.mkdir(nome_diretorio)
                print('Pronto!\n')
                os.system('espeak -v pt-br -g 4 -a 100 "Pronto"')
            except OSError:
                print('Diretorio já existe\n')
                os.system('espeak -v pt-br -g 4 -a 100 "Diretorio já existe"')

        elif(frase == u'criar arquivo'):
            nome_arquivo=raw_input('Insira o nome do arquivo: ')
            try:
                os.mkdir(pasta)
                os.chdir(os.getcwd()+'/'+pasta)
            except OSError:
                os.chdir(os.getcwd()+'/'+pasta)

            try:
                arquivo=open(nome_arquivo,'r')
                print('Já existe arquivo com esse nome')
                os.system('espeak -v pt-br -g 4 -a 100 "já existe arquivo com esse nome"')
            except IOError:
                arquivo=open(nome_arquivo,'w')
                print('Pronto! Arquivo salvo na pasta arquivos\n')
                os.system('espeak -v pt-br -g 4 -a 100 "Pronto! Arquivo salvo na pasta arquivos"')
                os.chdir(diretorio_atual)

    elif(palavras[0] == u'remover'):
        os.chdir(diretorio_atual)
        pasta='arquivos'
        if(tam == 3):
            if(palavras[1] == u'arquivo'):
                os.chdir(os.getcwd()+'/'+'arquivos')
                if(os.path.isfile(palavras[2])):
                    os.remove(palavras[2])
                    print('Removido')
                    os.system('espeak -v pt-br -g 4 -a 100 "Removido"')
                else:
                    print('arquivo não existe')
                    os.system('espeak -v pt-br -g 4 -a 100 "Arquivo não existe"')

            elif(palavras[1] == u'diretorio'):
                if(palavras[2] == u'modulos' or palavras[2] == u'teste' or palavras[2] == u'arquivos'):
                    print('Pastas protegidas, não podem ser apagadas')
                    os.system('espeak -v pt-br -g 4 -a 100 "pastas protegidas, não podem ser apagadas"')
                else:
                    try:
                        os.rmdir(palavras[2])
                        print('removido!\n')
                        os.system('espeak -v pt-br -g 4 -a 100 "removido"')
                    except OSError:
                        print('Diretorio não existe')
                        os.system('espeak -v pt-br -g 4 -a 100 "Diretório não existe"')


        elif(tam == 1):
            operacao=raw_input('Deseja remover arquivo ou diretorio? ')
            if(operacao == u'diretorio'):
                nome_diretorio=raw_input('Digite o nome do diretorio: ')
                if(nome_diretorio == u'modulos' or nome_diretorio == u'teste' or nome_diretorio == u'arquivos'):
                    print('Pastas protegidas, não podem ser apagadas')
                    os.system('espeak -v pt-br -g 4 -a 100 "pastas protegidas, não podem ser apagadas"')
                else:
                    try:
                        os.rmdir(nome_diretorio)
                        print('removido!\n')
                        os.system('espeak -v pt-br -g 4 -a 100 "removido"')
                    except OSError:
                        print('Diretorio não existe')
                        os.system('espeak -v pt-br -g 4 -a 100 "Diretório não existe"')

            elif(operacao == u'arquivo'):
                nome_arquivo=raw_input('Digite o nome do arquivo: ')
                os.chdir(os.getcwd()+'/'+'arquivos')
                if(os.path.isfile(nome_arquivo)):
                    os.remove(nome_arquivo)
                    print('Removido')
                    os.system('espeak -v pt-br -g 4 -a 100 "Removido"')
                else:
                    print('arquivo não existe')
                    os.system('espeak -v pt-br -g 4 -a 100 "Arquivo não existe"')

            else:
                print('Operação inválida\n')
                os.system('espeak -v pt-br -g 4 -a 100 "Operação Inválida"')

        elif(tam == 2):
            if(palavras[1] == u'diretorio'):
                nome_diretorio=raw_input('Digite o nome do diretorio: ')
                if(nome_diretorio == u'modulos' or nome_diretorio == u'teste' or nome_diretorio == u'arquivos'):
                    print('Pastas protegidas, não podem ser apagadas')
                    os.system('espeak -v pt-br -g 4 -a 100 "pastas protegidas, não podem ser apagadas"')
                else:
                    try:
                        os.rmdir(nome_diretorio)
                        print('removido!\n')
                        os.system('espeak -v pt-br -g 4 -a 100 "removido"')
                    except OSError:
                        print('Diretorio não existe')
                        os.system('espeak -v pt-br -g 4 -a 100 "Diretório não existe"')

            elif(palavras[1] == u'arquivo'):
                nome_arquivo=raw_input('Digite o nome do arquivo: ')
                os.chdir(os.getcwd()+'/'+'arquivos')
                if(os.path.isfile(nome_arquivo)):
                    os.remove(nome_arquivo)
                    print('Removido')
                    os.system('espeak -v pt-br -g 4 -a 100 "Removido"')
                else:
                    print('arquivo não existe')
                    os.system('espeak -v pt-br -g 4 -a 100 "Arquivo não existe"')

    elif(palavras[0] == u'editar'):
        tam=len(palavras)
        if(tam == 3):
            if(palavras[1] == u'arquivo'):
                try:
                    os.chdir(os.getcwd()+'/'+'arquivos')
                except OSError:
                    os.mkdir('arquivos')
                    os.chdir(os.getcwd()+'/'+'arquivos')
                os.system('xdg-open '+palavras[2])
            else:
                print('A penas possivel editar arquivos')
                os.system('espeak -v pt-br -g 4 -a 100 "A penas possivel editar arquivos"')
        elif(tam == 2):
            if(palavras[1] == u'arquivo'):
                nome_arquivo=raw_input('Insira o nome do arquivo: ')
                try:
                    os.chdir(os.getcwd()+'/'+'arquivos')
                except OSError:
                    os.mkdir('arquivos')
                    os.chdir(os.getcwd()+'/'+'arquivos')
                os.system('gedit '+nome_arquivo)
            else:
                print('A penas possivel editar arquivos')
                os.system('espeak -v pt-br -g 4 -a 100 "A penas possivel editar arquivos"')
        else:
            print('Sintaxe incorreta, digite ajuda para ver a documentação')
            os.system('espeak -v pt-br -g 4 -a 100 "Sintaxe incorreta, Digite ajuda para ver a documentação"')

    elif(palavras[0] == u'renomear'):
        tam=len(palavras)
        if(tam == 3):
            if(palavras[1] == u'arquivo'):
                try:
                    os.chdir(os.getcwd()+'/'+'arquivos')
                except OSError:
                    print('Não tem nenhum arquivo salvo')
                    os.system('espeak -v pt-br -g 4 -a 100 "Não tem nenhum arquivo salvo"')

                if(os.path.isfile(palavras[2])):
                    novo_nome=raw_input('Insira o novo nome: ')
                    os.rename(palavras[2],novo_nome)
                    print('Pronto')
                    os.system('espeak -v pt-br -g 4 -a 100 "Pronto"')
                else:
                    print('Arquivo não existe')
                    os.system('espeak -v pt-br -g 4 -a 100 "Arquivo não existe"')

            elif(palavras[1] == u'diretorio'):
                if(os.path.isdir(palavras[2])):
                    if(palavras[2] == u'modulos' or palavras[2] == u'arquivos'):
                        print('Não é permitido renomear diretorio modulos')
                        os.system('espeak -v pt-br -g 4 -a 100 "Não é permitido renomear o diretorio modulos"')
                    else:
                        novo_nome=raw_input('Digite novo nome do diretorio: ')
                        os.rename(palavras[2],novo_nome)
                        print('Pronto')
                        os.system('espeak -v pt-br -g 4 -a 100 "Pronto"')

            else:
                print('Só pode renomear um diretorio ou arquivo ')
                os.system('espeak -v pt-br -g 4 -a 100 "Só pode renomear um diretorio ou arquivo "')

        else:
            print('Sintaxe incorreta, digite ajuda para ver a documentação')
            os.system('espeak -v pt-br -g 4 -a 100 "Sintaxe incorreta, Digite ajuda para ver a documentação"')

    # toca música #
    elif(palavras[0] == u'tocar'):
        tam=len(palavras)
        if(tam == 1):
            tocar()
        elif(tam == 2):
            tocar(palavras[1])
        elif(tam == 3):
            tocar(palavras[1]+' '+palavras[2])
        elif(tam == 4):
            tocar(palavras[1]+' '+palavras[2]+' '+palavras[3])
        elif(tam == 5):
            tocar(palavras[1]+' '+palavras[2]+' '+palavras[3]+' '+palavras[4])
        elif(tam == 6):
            tocar(palavras[1]+' '+palavras[2]+' '+palavras[3]+' '+palavras[4]+' '+palavras[5])


    elif(frase == u'qual sua idade' or frase == u'qual sua idade?' or frase == u'quantos anos você tem?' or frase == u'quantos anos voce tem?' or frase == u'quantos anos voce tem?' or frase == u'quantos anos você tem?' or frase == u'quantos anos você tem'):
        now=datetime.now()
        ano=now.year
        mes=now.month
        dia=now.day
        atual_ano=ano-nascimento_ano
        atual_mes=mes-nascimento_mes
        atual_dia=dia-nascimento_dia
        print('Eu tenho')
        naotem=0
        if(atual_ano!=0):
            print(str(atual_ano)+' anos')
        else:
            naotem=naotem+1
        if(atual_mes!=0):
            print(str(atual_mes)+' meses')
        else:
            naotem=naotem+1
        print(str(-atual_dia)+' dias')
        if(atual_ano!=0):
            a='Eu tenho '+str(atual_ano)+' anos '+str(atual_mes)+' meses e ' +str(-atual_dia)+' dias de idade'
        if(atual_ano == 0):
            a='Eu tenho '+str(atual_mes)+' meses e ' +str(-atual_dia)+' dias de idade'
        if(naotem == 2):
            a='Eu tenho '+str(-atual_dia)+' dias de idade'

        os.system('espeak -v pt-br -g 4 -a 100 "'+a+'"')


    # esvazia a lixeira #
    elif(frase == u'esvaziar lixeira' or frase == u'esvaziar'):
        #os.system('./esvaziar.sh')
        os.chdir(os.environ['HOME']+'/.local/share/Trash/files')
        a=os.listdir(os.environ['HOME']+'/.local/share/Trash/files')
        for elemento in a:
            try:
                print('removendo -> ' + str(elemento))
                os.remove(elemento)
            except OSError:
                print('removendo -> ' + str(elemento))
                os.system('rm -r '+ elemento)
        print('Pronto!\n')
        os.system('espeak -v pt-br -g 4 -a 100 "Pronto!"')

    elif(frase == u'calculadora'):
        os.system('gnome-calculator')

    elif(frase == u'history' or frase == u'historico' or frase == u'histórico' or frase == u'historico ' or frase == u'histórico '):
        print('Histórico: \n')
        for comandos in lista:
            print(str(comandos))

    elif(frase == u'onde estou?'or frase == u'onde estou' or frase == u'qual minha localizacao' or frase == u'qual minha localização?' or frase == u'qual minha localização' or frase == u'localização' or frase == u'localizacao'):
        minha_localizacao('estado')
    elif(frase == u'qual meu pais' or frase == u'qual meu país?' or frase == u'qual meu país' or frase == u'qual meu pais?' or frase == u'pais'):
        minha_localizacao('pais')
    elif(frase == u'qual meu ip externo?' or frase == u'qual meu ip' or frase == u'ip' or frase == u'qual meu ip?'):
        minha_localizacao('ip')

    elif(palavras[0] == u'clima'):
        tam=len(palavras)
        if(tam == 2):
            cidade=palavras[1]
        elif(tam == 3):
            cidade=palavras[1]+' '+palavras[2]
        elif(tam == 4):
            cidade=palavras[1]+' '+palavras[2]+' '+palavras[3]
        clima(cidade)

    # procura filme #
    elif(palavras[0] == u'procurar'):
        if(palavras[1] == u'filme'):
            if(tam == 3):
                filmes(palavras[2])
            if(tam == 4):
                nome_filme=palavras[2]+' '+palavras[3]
                filmes(nome_filme)
            elif(tam == 5):
                nome_filme=palavras[2]+' '+palavras[3]+' '+palavras[4]
                filmes(nome_filme)
            elif(tam == 6):
                nome_filme=palavras[2]+' '+palavras[3]+' '+palavras[4]+' '+palavras[5]
                filmes(nome_filme)
        elif(palavras[1] == u'serie'): # pesquisa serie
            print('ainda não disponivel')

        else:#procura no google
            a=1

    # verifica a cotação da moeda #
    elif(palavras[0] == u'cotacao' or palavras[0] == u'cotação'):
        if(tam>1):
            if(palavras[1] == u'dolar'):
                cotacao('USD')
            elif(palavras[1] == u'euro'):
                cotacao('EUR')
            elif(palavras[1] == u'bitcoin' or palavras[1] == u'btc'):
                cotacao('BTC')
            else:
                print('Moeda Indisponível ou não existe\n')
                os.system('espeak -v pt-br -g 4 -a 100 "Moeda Indisponível ou não existe"')

    elif(palavras[0] == lista_perguntas[0] or palavras[0] == lista_perguntas[1]):
        onde(palavras)
        tam=len(palavras)
        if(tam == 3):
            busca(palavras[2])
        elif(tam == 4):
            busca(palavras[2]+' '+palavras[3])
        elif(tam == 5):
            busca(palavras[2]+' '+palavras[3]+' '+palavras[4])
        elif(tam == 6):
            busca(palavras[2]+' '+palavras[3]+' '+palavras[4]+' '+palavras[5])
        elif(tam == 7):
            busca(palavras[2]+' '+palavras[3]+' '+palavras[4]+' '+palavras[6]+' '+palavras[7])

    elif(palavras[0] == u'quem' or palavras[0] == u'qm'):
        tam=len(palavras)
        if(tam == 1):
            print('Sintaxe incorreta')
            os.system('espeak -v pt-br -g 4 -a 100 "Sintaxe incorreta"')
        elif(palavras[1] == u'é' or palavras[1] == u'e' or palavras[1] == u'eh' or palavras[1] == u'foi' or palavras[1] == u'era'):
            if(tam == 2):
                print('Sintaxe incorreta')
                os.system('espeak -v pt-br -g 4 -a 100 "Sintaxe incorreta"')
            elif(tam == 3):
                busca(palavras[2])
            elif(tam == 4):
                busca(palavras[2]+' '+palavras[3])
            elif(tam == 5):
                busca(palavras[2]+' '+palavras[3]+' '+palavras[4])
            elif(tam == 6):
                busca(palavras[2]+' '+palavras[3]+' '+palavras[4]+' '+palavras[5])
            elif(tam == 7):
                busca(palavras[2]+' '+palavras[3]+' '+palavras[4]+' '+palavras[6]+' '+palavras[7])

        else:
            print('Sintaxe incorreta')
            os.system('espeak -v pt-br -g 4 -a 100 "Sintaxe incorreta"')

    elif(palavras[0] == u'busca' or palavras[0] == u'buscar'):
        tam=len(palavras)
        if(tam == 1):
            print('Sintaxe incorreta')
        elif(tam == 2):
            busca(palavras[1])
        elif(tam == 3):
            busca(palavras[1]+' '+palavras[2])
        elif(tam == 4):
            busca(palavras[1]+' '+palavras[2]+' '+palavras[3])
        elif(tam == 5):
            busca(palavras[1]+' '+palavras[2]+' '+palavras[3]+' '+palavras[4])
        elif(tam == 6):
            busca(palavras[1]+' '+palavras[2]+' '+palavras[3]+' '+palavras[4]+' '+palavras[5])



    # ENVIO DE EMAILS COM NOTIFICAÇÕES DE NOVIDADES #
    elif(palavras[0] == u'email'):

        enviado=0
        try:
            arquivo=open('config/email','r')
            email=arquivo.readline()
            if(email == u''): # Se o cara interromper, ele salva como arquivo vazio
                enviado=0
                raise KeyboardInterrupt
            envia_email(email)
            enviado=1
        except:
            arquivo=open('config/email.txt','w')

        if(enviado == 0):

            teste=raw_input('Digite o seu email, para enviar notificações: ')
            padrao=re.findall(r'[\w\.-]+@[\w-]+\.[\w\.-]+',teste)

            if(padrao == []):
                print('O digitado não é válido como email')

            else:
                arquivo=open('config/email.txt','a')
                arquivo.write(teste)
                envia_email(teste)
                print('Seu email está configurado')
        arquivo.close()



    # ler arquivo agendar com -> abrir arquivo
    elif(palavras[0] == u'agenda' or palavras[0] == u'agendar' or palavras[0] == u'salvar'):
        tam=len(palavras)
        if(tam == 2):
            Agenda(palavras[1])
        elif(tam == 1):
            Agenda(None)

    else:
        x=random.randrange(1,5)
        if(x == 1):
            print('Não entendi, poderia repetir ?')
            os.system('espeak -v pt-br -g 4 -a 100 "Não entendi, poderia repetir ?"')
        elif(x == 2):
            print('O que você quis dizer ?')
            os.system('espeak -v pt-br -g 4 -a 100 "O que você quis dizer ?"')
        elif(x == 3):
            print('Pode falar novamente ?')
            os.system('espeak -v pt-br -g 4 -a 100 "Pode falar novamente ?"')
        else:
            print('O que você quer dizer com isso ?')
            os.system('espeak -v pt-br -g 4 -a 100 "O que você quer dizer com isso ?"')
