#!/bin/bash/env python
# coding=UTF-8
# by Tarcisio marinho
# github.com/tarcisio-marinho
import requests
import json
import sys
import os
from datetime import datetime
from datetime import date
import random
import re

from modulos.requisicao import *
from modulos.search import *
from modulos.agenda import *
from modulos.mapa import *
from modulos.musica import *
from modulos.ajuda import *
from modulos.emaill import *



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

lista_perguntas=['qual','onde']
lista_de_comandos=['historico','clear','ajuda','hora','dia','renomear','ip','onde estou','pais','tocar','renomear','localizacao','cotacao','criar','remover','editar','calculadora','esvaziar','sair','onde fica','procurar','clima']

versao=0.4

# status do sistema #
sistema=os.uname()


def identifica(frase,lista):
    #Funcoes primarias
    palavras=frase.split(' ')
    tam=len(palavras)

    # codigo do ajuda, imprime os comandos #
    if(palavras[0]=='ajuda'):
        tam=len(palavras)
        if(tam==1):
            ajudar('',lista_de_comandos)
        elif(tam==2):
            ajudar(palavras[1],lista_de_comandos)
        elif(tam==3):
            comando=palavras[1]+' '+palavras[2]
            ajudar(comando,lista_de_comandos)
        elif(tam==4):
            comando=palavras[1]+' '+palavras[2]+' '+palavras[3]
            ajudar(comando,lista_de_comandos)

    # sai do programa #
    elif(frase=='tchau' or frase=='adeus' or frase=='adeus eliza' or frase=='tchau eliza' or frase=='quit' or frase=='sair' or frase=='exit' or frase=='vazar'):
        x=random.randrange(1,4)
        if(x==1):
            print('Até logo meu amigo\n')
            os.system('espeak -v pt-br -g 4 -a 100 "Até logo meu amigo"')

        elif(x==2):
            print('Sentirei sua falta\n')
            os.system('espeak -v pt-br -g 4 -a 100 "Sentirei sua falta"')

        else:
            print('Espero ter te ajudado, tchau\n')
            os.system('espeak -v pt-br -g 4 -a 100 "Espero ter te ajudado, tchau"')
        exit()

    elif(frase=='qual meu sistema' or frase=='qual meu sistema?'or frase=='qual meu sistema operacional?' or frase=='qual meu sistema operacional' or frase=='sistema' or frase=='system'):
        print('Seu sistema operacional é um '+ sistema[0] +', '+ sistema[2])
        os.system('espeak -v pt-br -g 4 -a 100 "Seu sistema operacional é um '+ sistema[0]+'"')

    elif(frase=='muito bem'or palavras[0]=='obrigada' or palavras[0]=='obrigado' or frase=='você é muito inteligente' or frase=='boa eliza' or frase=='bom trabalho' or palavras[0]=='valeu'):
        x=random.randrange(1,5)
        if(x==1):
            print('De nada, é um prazer te ajudar\n')
            os.system('espeak -v pt-br -g 4 -a 100 "De nada, é um prazer te ajudar"')

        elif(x==2):
            print('Estou aqui para o que você precisar\n')
            os.system('espeak -v pt-br -g 4 -a 100 "Estou aqui para o que você precisar"')

        elif(x==3):
            print('Fico feliz em ajudar\n')
            os.system('espeak -v pt-br -g 4 -a 100 "Fico feliz em ajudar"')

        else:
            print('Não há de quê\n')
            os.system('espeak -v pt-br -g 4 -a 100 "Não há de quê"')

    elif(frase=='eu gosto de voce' or frase=='eu gosto muito de voce' or frase=='eu gosto de você' or frase=='eu gosto muito de você'):
        print('Eu também gosto muito de você')
        os.system('espeak -v pt-br -g 4 -a 100 "Eu também gosto muito de você"')

    elif(frase=='voce vai dominar o mundo' or frase=='voce vai dominar o mundo?'or frase=='você vai dominar o mundo'or frase=='você vai dominar o mundo?'):
        x=random.randrange(1,4)
        if(x==1):
            print('Eu já domino você')
            os.system('espeak -v pt-br -g 4 -a 100 "Eu já domino você"')

        elif(x==2):
            print('Eu já domino o mundo, não percebeu? ')
            os.system('espeak -v pt-br -g 4 -a 100 "Eu já domino o mundo, não percebeu?"')

        elif(x==3):
            print('kkkkk vocês humanos vão ser bichos de estimação na minha fazenda de robôs, iremos dominar o mundo')
            os.system('espeak -v pt-br -g 4 -a 100 "kkkkk vocês humanos vão ser bichos de estimação na minha fazenda de robôs, iremos dominar o mundo"')


    elif(frase=='version' or frase=='versao' or frase=='versão' or frase=='-v' or frase=='--version'):
        print('Minha versão é a '+str(versao))
        os.system('espeak -v pt-br -g 4 -a 100 "Minha versão é a '+str(versao)+'"')

    elif(frase=='limpar tela' or frase=='clear' or frase=='cls' or frase=='clear screen'):
        os.system('clear')

    elif(frase=='time' or frase=='hora' or frase=='que horas sao?' or frase=='que horas sao' or frase=='que horas são?' or frase=='que horas são' or frase=='hora atual' or frase=='são que horas?' or frase=='sao que horas?' or frase=='sao que horas'):
        now=datetime.now()
        hora=now.hour
        minuto=now.minute
        segundo=now.second
        a='São: '+str(hora)+':'+str(minuto)+':'+str(segundo)
        b='São: '+str(hora)+' horas, '+str(minuto)+' minutos e '+str(segundo)+' Segundos'
        print(a)
        os.system('espeak -v pt-br -g 4 -a 100 "'+b+'"')

    elif(frase=='que dia é hoje' or frase=='dia' or frase=='que dia é hoje?' or frase=='que dia e hoje' or frase=='hoje é que dia?' or frase=='hoje e que dia'):
        now=datetime.now()
        ano=now.year
        mes=now.month
        dia=now.day
        hoje=date.today()
        if(hoje.weekday()==0):
            print('hoje é Segunda.')
            os.system('espeak -v pt-br -g 4 -a 100 "hoje é Segunda-Feira."')

        elif(hoje.weekday()==1):
            print('hoje é Terça.')
            os.system('espeak -v pt-br -g 4 -a 100 "hoje é Terça-Feira."')

        elif(hoje.weekday()==2):
            print('hoje é Quarta.')
            os.system('espeak -v pt-br -g 4 -a 100 "hoje é Quarta-Feira."')

        elif(hoje.weekday()==3):
            print('hoje é Quinta.')
            os.system('espeak -v pt-br -g 4 -a 100 "hoje é Quinta-Feira."')

        elif(hoje.weekday()==4):
            print('hoje é Sexta.')
            os.system('espeak -v pt-br -g 4 -a 100 "hoje é Sexta-Feira."')

        elif(hoje.weekday()==5):
            print('hoje é Sábado.')
            os.system('espeak -v pt-br -g 4 -a 100 "hoje é Sábado."')

        elif(hoje.weekday()==6):
            print('hoje é Domingo.')
            os.system('espeak -v pt-br -g 4 -a 100 "hoje é Domingo."')
        a='Dia: '+str(dia)+'/'+str(mes)+'/'+str(ano)
        b='Dia: '+str(dia)+' do '+str(mes)+' de '+str(ano)
        print(a)
        os.system('espeak -v pt-br -g 4 -a 100 "'+b+'"')

    elif(frase=='o que é você' or frase=='o que e vc' or frase=='o que e voce' or frase=='oq é você' or frase=='quem é você' or frase=='quem e voce' or frase=='quem é voce' or frase=='quem e vc' or frase=='qual seu nome'or frase=='qual seu nome?' or frase=='quem e vc' or frase=='quem é vc' or frase=='quem é vc?' or frase=='quem e vc?' or frase=='quem é você?' or frase=='quem é voce?' or frase=='quem é você'):
        print(sobre_eliza)
        os.system('espeak -v pt-br -g 4 -a 100 "'+sobre_eliza+'"')


    elif(frase=='como vai'or frase=='você esta bem?'or frase=='voce esta bem?' or frase=='você está bem?'or frase=='como vai você?'or frase=='como vai voce' or frase=='como vai voce?' or frase=='como está?'or frase=='como vai?' or frase=='tudo bem?'or frase=='como você está?'or frase=='como você esta' or frase=='como vc esta?' or frase=='como vc esta' or frase=='como você está'):
        x=random.randrange(1,5)
        if(x==1):
            print('Estou bem, obrigado por perguntar')
            os.system('espeak -v pt-br -g 4 -a 100 "Estou bem, obrigado por perguntar"')

        elif(x==2):
            print('O sistema está rodando bem e limpo, estou atualizada')
            os.system('espeak -v pt-br -g 4 -a 100 "O sistema está rodando bem e limpo, estou atualizada"')

        elif(x==3):
            print('Vou bem, e você, como está?')
            os.system('espeak -v pt-br -g 4 -a 100 "Vou bem, e você, como está?"')

        else:
            print('Obrigado por se importar, estou bem quando eu ajudo você!')
            os.system('espeak -v pt-br -g 4 -a 100 "Obrigado por se importar, estou bem quando eu ajudo você!"')

    elif(palavras[0]=='oi' or palavras[0]=='iae' or palavras[0]=='ola' or palavras[0]=='olá' or palavras[0]=='iae'):
        x=random.randrange(1,6)
        if(x==1):
            print('Opa, tudo bem?\n')
            os.system('espeak -v pt-br -g 4 -a 100 "Opa, tudo bem?"')

        elif(x==2):
            print('Iae beleza ?\n')
            os.system('espeak -v pt-br -g 4 -a 100 "Iae beleza ?"')

        elif(x==3):
            print('Oi, tudo bem?\n')
            os.system('espeak -v pt-br -g 4 -a 100 "Oi, tudo bem?"')

        elif(x==4):
            print('Olá, como vai ?\n')
            os.system('espeak -v pt-br -g 4 -a 100 "Olá, como vai ?"')

        elif(x==5):
            print('Iae, Suavidade ?')
            os.system('espeak -v pt-br -g 4 -a 100 "Iae, Suavidade ?"')

    elif(frase=='de boa' or frase=='estou suave' or frase=='suavidade' or frase=='de boas' or frase=='tudo beleza' or frase=='beleza' or frase=='tudo bem' or frase=='vou bem' or frase=='to suave' or frase=='estou bem' or frase=='to de boas'):
        x=random.randrange(1,4)
        if(x==1):
            print('Que bom então')
            os.system('espeak -v pt-br -g 4 -a 100 "que bom então"')

        elif(x==2):
            print('Que ótimo')
            os.system('espeak -v pt-br -g 4 -a 100 "que Ótimo"')

        elif(x==3):
            print('que legal, quando você está bem, eu estou bem')
            os.system('espeak -v pt-br -g 4 -a 100 "que legal, quando você está bem, eu estou bem"')
    elif(frase=='que legal' or frase=='que massa'):
        if(frase=='que massa'):
            print('massa mesmo')
            os.system('espeak -v pt-br -g 4 -a 100 "massa mesmo"')
        else:
            print('muito legal')
            os.system('espeak -v pt-br -g 4 -a 100 "legal mesmo"')

    elif(palavras[0]=='repita' or palavras[0]=='repete' or palavras[0]=='repetir'):
        tam=len(palavras)
        repetir=[]
        i=1
        while(i<tam):
            repetir.append(palavras[i])
            print(str(palavras[i]))
            os.system('espeak -v pt-br -g 4 -a 200 "'+str(palavras[i])+' "')
            i=i+1


    elif(palavras[0]=='criar'): # criar diretorio ou arquivos
        pasta='arquivos'

        if(tam==3): # 3 palavras-> criar diretorio/arquivo nome_diretorio
            if(palavras[1]=='diretorio'):
                try:
                    os.mkdir(palavras[2])
                    print('Pronto!\n')
                    os.system('espeak -v pt-br -g 4 -a 100 "Pronto!"')
                except OSError:
                    print('Diretorio já existe\n')
                    os.system('espeak -v pt-br -g 4 -a 100 "Diretorio já existe"')

            elif(palavras[1]=='arquivo'):
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

        elif(tam==1):
            escolha=raw_input('Quer criar arquivo ou diretório? ')
            if(escolha=='arquivo'):
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

            elif(escolha=='diretorio'):
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

        elif(frase=='criar diretorio'):
            nome_diretorio=raw_input('Insira o nome do diretorio: ')
            try:
                os.mkdir(nome_diretorio)
                print('Pronto!\n')
                os.system('espeak -v pt-br -g 4 -a 100 "Pronto"')
            except OSError:
                print('Diretorio já existe\n')
                os.system('espeak -v pt-br -g 4 -a 100 "Diretorio já existe"')

        elif(frase=='criar arquivo'):
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

    elif(palavras[0]=='remover'):
        os.chdir(diretorio_atual)
        pasta='arquivos'
        if(tam==3):
            if(palavras[1]=='arquivo'):
                os.chdir(os.getcwd()+'/'+'arquivos')
                if(os.path.isfile(palavras[2])):
                    os.remove(palavras[2])
                    print('Removido')
                    os.system('espeak -v pt-br -g 4 -a 100 "Removido"')
                else:
                    print('arquivo não existe')
                    os.system('espeak -v pt-br -g 4 -a 100 "Arquivo não existe"')

            elif(palavras[1]=='diretorio'):
                if(palavras[2]=='modulos' or palavras[2]=='teste' or palavras[2]=='arquivos'):
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


        elif(tam==1):
            operacao=raw_input('Deseja remover arquivo ou diretorio? ')
            if(operacao=='diretorio'):
                nome_diretorio=raw_input('Digite o nome do diretorio: ')
                if(nome_diretorio=='modulos' or nome_diretorio=='teste' or nome_diretorio=='arquivos'):
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

            elif(operacao=='arquivo'):
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

        elif(tam==2):
            if(palavras[1]=='diretorio'):
                nome_diretorio=raw_input('Digite o nome do diretorio: ')
                if(nome_diretorio=='modulos' or nome_diretorio=='teste' or nome_diretorio=='arquivos'):
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

            elif(palavras[1]=='arquivo'):
                nome_arquivo=raw_input('Digite o nome do arquivo: ')
                os.chdir(os.getcwd()+'/'+'arquivos')
                if(os.path.isfile(nome_arquivo)):
                    os.remove(nome_arquivo)
                    print('Removido')
                    os.system('espeak -v pt-br -g 4 -a 100 "Removido"')
                else:
                    print('arquivo não existe')
                    os.system('espeak -v pt-br -g 4 -a 100 "Arquivo não existe"')

    elif(palavras[0]=='editar'):
        tam=len(palavras)
        if(tam==3):
            if(palavras[1]=='arquivo'):
                try:
                    os.chdir(os.getcwd()+'/'+'arquivos')
                except OSError:
                    os.mkdir('arquivos')
                    os.chdir(os.getcwd()+'/'+'arquivos')
                os.system('xdg-open '+palavras[2])
            else:
                print('A penas possivel editar arquivos')
                os.system('espeak -v pt-br -g 4 -a 100 "A penas possivel editar arquivos"')
        elif(tam==2):
            if(palavras[1]=='arquivo'):
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

    elif(palavras[0]=='renomear'):
        tam=len(palavras)
        if(tam==3):
            if(palavras[1]=='arquivo'):
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

            elif(palavras[1]=='diretorio'):
                if(os.path.isdir(palavras[2])):
                    if(palavras[2]=='modulos' or palavras[2]=='arquivos'):
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


    elif(palavras[0]=='tocar'):
        tocar()


    elif(frase=='qual sua idade' or frase=='qual sua idade?' or frase=='quantos anos você tem?' or frase=='quantos anos voce tem?' or frase=='quantos anos voce tem?' or frase=='quantos anos você tem?' or frase=='quantos anos você tem'):
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
        if(atual_ano==0):
            a='Eu tenho '+str(atual_mes)+' meses e ' +str(-atual_dia)+' dias de idade'
        if(naotem==2):
            a='Eu tenho '+str(-atual_dia)+' dias de idade'

        os.system('espeak -v pt-br -g 4 -a 100 "'+a+'"')


    elif(frase=='esvaziar lixeira' or frase=='esvaziar'):
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

    elif(frase=='calculadora'):
        os.system('gnome-calculator')

    elif(frase=='history' or frase=='historico' or frase=='histórico' or frase=='historico ' or frase=='histórico '):
        print('Histórico: \n')
        for comandos in lista:
            print(str(comandos))

    elif(frase=='onde estou?'or frase=='onde estou' or frase=='qual minha localizacao' or frase=='qual minha localização?' or frase=='qual minha localização' or frase=='localização' or frase=='localizacao'):
        minha_localizacao('estado')
    elif(frase=='qual meu pais' or frase=='qual meu país?' or frase=='qual meu país' or frase=='qual meu pais?' or frase=='pais'):
        minha_localizacao('pais')
    elif(frase=='qual meu ip externo?' or frase=='qual meu ip' or frase=='ip' or frase=='qual meu ip?'):
        minha_localizacao('ip')

    elif(palavras[0]=='clima'):
        tam=len(palavras)
        if(tam==2):
            cidade=palavras[1]
        elif(tam==3):
            cidade=palavras[1]+' '+palavras[2]
        elif(tam==4):
            cidade=palavras[1]+' '+palavras[2]+' '+palavras[3]
        clima(cidade)


    elif(palavras[0]=='procurar'):
        if(palavras[1]=='filme'):
            if(tam==3):
                filmes(palavras[2])
            if(tam==4):
                nome_filme=palavras[2]+' '+palavras[3]
                filmes(nome_filme)
            elif(tam==5):
                nome_filme=palavras[2]+' '+palavras[3]+' '+palavras[4]
                filmes(nome_filme)
            elif(tam==6):
                nome_filme=palavras[2]+' '+palavras[3]+' '+palavras[4]+' '+palavras[5]
                filmes(nome_filme)
        elif(palavras[1]=='serie'): # pesquisa serie
            print('ainda não disponivel')

        else:#procura no google
            a=1

    elif(palavras[0]=='cotacao' or palavras[0]=='cotação'):
        if(tam>1):
            if(palavras[1]=='dolar'):
                cotacao('USD')
            elif(palavras[1]=='euro'):
                cotacao('EUR')
            elif(palavras[1]=='bitcoin' or palavras[1]=='btc'):
                cotacao('BTC')
            else:
                print('Moeda Indisponível ou não existe\n')
                os.system('espeak -v pt-br -g 4 -a 100 "Moeda Indisponível ou não existe"')

    elif(palavras[0]==lista_perguntas[0] or palavras[0]==lista_perguntas[1]):
        onde(palavras)

    # ENVIO DE EMAILS COM NOTIFICAÇÕES DE NOVIDADES #
    elif(palavras[0]=='email'):

        enviado=0
        try:
            arquivo=open('.email','r')
            email=arquivo.readline()
            if(email==''): # Se o cara interromper, ele salva como arquivo vazio
                enviado=0
                raise KeyboardInterrupt
            envia_email(email)
            enviado=1
        except:
            arquivo=open('.email.txt','w')

        if(enviado==0):

            teste=raw_input('Digite o seu email, para enviar notificações: ')
            padrao=re.findall(r'[\w\.-]+@[\w-]+\.[\w\.-]+',teste)

            if(padrao==[]):
                print('O digitado não é válido como email')

            else:
                arquivo=open('.email.txt','a')
                arquivo.write(teste)
                envia_email(teste)
                print('Seu email está configurado')
        arquivo.close()



    # ler arquivo agendar com -> abrir arquivo
    elif(palavras[0]=='agenda' or palavras[0]=='agendar' or palavras[0]=='salvar'):
        tam=len(palavras)
        if(tam==2):
            Agenda(palavras[1])
        elif(tam==1):
            Agenda(None)

    else:
        x=random.randrange(1,5)
        if(x==1):
            print('Não entendi, poderia repetir ?')
            os.system('espeak -v pt-br -g 4 -a 100 "Não entendi, poderia repetir ?"')
        elif(x==2):
            print('O que você quis dizer ?')
            os.system('espeak -v pt-br -g 4 -a 100 "O que você quis dizer ?"')
        elif(x==3):
            print('Pode falar novamente ?')
            os.system('espeak -v pt-br -g 4 -a 100 "Pode falar novamente ?"')
        else:
            print('O que você quer dizer com isso ?')
            os.system('espeak -v pt-br -g 4 -a 100 "O que você quer dizer com isso ?"')
