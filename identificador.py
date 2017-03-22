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
import requisicao

sobre_eliza='''
Opa! Sou eliza uma assistente pessoal para o linux!
Fui criada para ajudar você :-)

Digite Help para ajuda nos comandos basicos
'''
comandos='''
Olá, sou Eliza, uma assistente pessoal para linux!
Os comandos basicos são:

[+] cotacao (moeda) - mostra a cotação da moeda atualmente
[+] criar diretorio (nome_do_diretorio) - cria diretorio
[+] criar arquivo (nome_do_arquivo) - cria arquivo
[+] dia - mostra o dia atual
[+] hora - mostra a hora
[+] versão - imprime na tela a versão de Eliza
[+] ajuda - imprime essa mensagem
[+] limpar tela - limpa a tela
[+] sair - sair

'''

nascimento_dia=17
nascimento_mes=3
nascimento_ano=2017



versao='Versão 1.0'

#API'S
#youtube- recomendados - novos videos
#twitch - principais streamers
#
#tocar(musica)
#ler(livro)
#youtube(nome_video)
#busca(google_nome)
#esvaziar_lixeira()
#atividades(){
#  print(atividades.txt)
#}
#ligarssh
# que horas sao

# o que é fecicidade, amor, sentimentos em geral
#sentido da vida
#voce é feliz ?

# eu gosto muito de voce
# voce é muito util para mim
# obrigado $USER

# abrir calculadora

def identifica(frase):
    #Funcoes primarias
    palavras=frase.split(' ')
    tam=len(palavras)

    if(frase=='quit' or frase=='sair' or frase=='exit' or frase=='vazar'):
        print('Até logo, sentirei sua falta\n')
        exit()

    elif(frase=='help' or frase=='ajuda' or frase=='tutorial' or frase=='list' or frase=='listar comandos' or frase=='listar'):
        print(comandos)

    elif(frase=='obrigado' or frase=='você é muito inteligente' or frase=='boa eliza' or frase=='bom trabalho' or frase=='valeu'):
        x=random.randrange(1,4)
        if(x==1):
            print('De nada, é um prazer te ajudar\n')
        elif(x==2):
            print('Que isso\n')
        elif(x==3):
            print('Obrigada\n')

    elif(frase=='version' or frase=='versao' or frase=='versão' or frase=='-v' or frase=='--version'):
        print(versao)

    elif(frase=='limpar tela' or frase=='clear' or frase=='cls' or frase=='clear screen'):
        os.system('clear')

    elif(frase=='time' or frase=='hora' or frase=='que horas sao?' or frase=='que horas sao' or frase=='que horas são?' or frase=='que horas são' or frase=='hora atual' or frase=='são que horas?' or frase=='sao que horas?' or frase=='sao que horas'):
        now=datetime.now()
        hora=now.hour
        minuto=now.minute
        segundo=now.second
        print('São: '+str(hora)+':'+str(minuto)+':'+str(segundo))

    elif(frase=='que dia é hoje' or frase=='dia' or frase=='que dia é hoje?' or frase=='que dia e hoje' or frase=='hoje é que dia?' or frase=='hoje e que dia'):
        now=datetime.now()
        ano=now.year
        mes=now.month
        dia=now.day
        hoje=date.today()
        if(hoje.weekday()==0):
            print('hoje é Segunda.')
        elif(hoje.weekday()==1):
            print('hoje é Terça.')
        elif(hoje.weekday()==2):
            print('hoje é Quarta.')
        elif(hoje.weekday()==3):
            print('hoje é Quinta.')
        elif(hoje.weekday()==4):
            print('hoje é Sexta.')
        elif(hoje.weekday()==5):
            print('hoje é Sábado.')
        elif(hoje.weekday()==6):
            print('hoje é Domingo.')
        print('Dia: '+str(dia)+'/'+str(mes)+'/'+str(ano))

    elif(frase=='quem e vc' or frase=='quem é vc' or frase=='quem é vc?' or frase=='quem e vc?' or frase=='quem é você?' or frase=='quem é voce?' or frase=='quem é você'):
        print(sobre_eliza)

    elif(frase=='oi eliza' or frase=='tudo bem?' or frase=='tudo bem'or frase=='oi' or frase=='ola' or frase=='olá' or frase=='oi tudo bem?' or frase=='iae' or frase=='oi tudo bem?'):
        x=random.randrange(1,5)
        if(x==1):
            print('Opa, tudo bem?\n')
        elif(x==2):
            print('Iae beleza ?\n')
        elif(x==3):
            print('Oi, tudo bem?\n')
        elif(x==4):
            print('Olá, como vai ?\n')

    elif(palavras[0]=='criar'): # criar diretorio ou arquivos
        if(tam==3): # 3 palavras-> criar diretorio/arquivo nome_diretorio
            if(palavras[1]=='diretorio'):
                try:
                    os.system('cd')
                    os.mkdir(palavras[2])
                    print('Pronto!\n')
                except OSError:
                    print('Diretorio já existe\n')

            elif(palavras[1]=='arquivo'):
                os.system('touch '+palavras[2])
                print('Pronto!\n')
        elif(tam==1):

            escolha=raw_input('Quer criar arquivo ou diretorio? ')
            if(escolha=='arquivo'):
                nome_arquivo=raw_input('Insira o nome do arquivo: ')
                os.system('touch '+nome_arquivo)
                print('Pronto!\n')

            elif(escolha=='diretorio'):
                nome_diretorio=raw_input('Insira o nome do diretorio: ')
                try:
                    os.mkdir(nome_diretorio)
                    print('Pronto!\n')
                except OSError:
                    print('Diretorio já existe\n')
            else:
                print('escolha invalida\n')

        elif(frase=='criar diretorio'):
            nome_diretorio=raw_input('Insira o nome do diretorio: ')
            try:
                os.mkdir(nome_diretorio)
                print('Pronto!\n')
            except OSError:
                print('Diretorio já existe\n')
        elif(frase=='criar arquivo'):
            nome_arquivo=raw_input('Insira o nome do arquivo: ')
            os.system('touch '+nome_arquivo)
            print('Pronto!\n')

    elif(palavras[0]=='remover'):
        if(tam==3):
            if(palavras[1]=='arquivo'):
                os.system('rm '+palavras[2])
                print('Pronto!\n')
            elif(palavras[1]=='diretorio'):
                os.system('rm -r '+palavras[2])
                print('Pronto!\n')
        elif(tam==1):
            operacao=raw_input('Deseja remover arquivo ou diretorio? ')
            if(operacao=='diretorio'):
                nome_diretorio=raw_input('Digite o nome do diretorio: ')
                os.system('rm -r '+nome_diretorio)
                print('Pronto!\n')
            elif(operacao=='arquivo'):
                nome_arquivo=raw_input('Digite o nome do arquivo: ')
                os.system('rm '+nome_arquivo)
                print('Pronto!\n')
            else:
                print('Operação inválida\n')
        elif(tam==2):
            if(palavras[1]=='diretorio'):
                nome_diretorio=raw_input('Digite o nome do diretorio: ')
                os.system('rm -r '+nome_diretorio)
                print('Pronto!\n')
            elif(palavras[1]=='arquivo'):
                nome_arquivo=raw_input('Digite o nome do arquivo: ')
                os.system('rm '+nome_arquivo)
                print('Pronto!\n')

    elif(frase=='qual sua idade' or frase=='qual sua idade?' or frase=='quantos anos você tem?' or frase=='quantos anos voce tem?' or frase=='quantos anos voce tem?' or frase=='quantos anos você tem?'):
        now=datetime.now()
        ano=now.year
        mes=now.month
        dia=now.day
        atual_ano=ano-nascimento_ano
        atual_mes=mes-nascimento_mes
        atual_dia=dia-nascimento_dia
        if(atual_ano!=0):
            print(str(atual_ano)+' anos')
        if(atual_mes!=0):
            print(str(atual_mes)+' meses')
        print(str(atual_dia)+' dias')


    #elif(frase=='tocar'):
    #    artista=raw_input('Artista: ')
    #    os.system('./tocar.sh '+ artista)




    ## CONTINUAR COM CONFIGURACOES DO SISTEMA


    elif(palavras[0]=='procurar'):
        if(tam==3):
            if(palavras[1]=='filme'):
                requisicao.filmes(palavras[2])
        if(tam>3):
            nome_filme=palavras[2]+' '+palavras[3]
            requisicao.filmes(nome_filme)


    elif(palavras[0]=='cotacao'):
        if(tam>1):
            if(palavras[1]=='dolar'):
                requisicao.cotacao('USD')
            elif(palavras[1]=='euro'):
                requisicao.cotacao('EUR')
            elif(palavras[1]=='bitcoin' or palavras[1]=='btc'):
                requisicao.cotacao('BTC')
            else:
                print('Moeda Indisponível ou não existe\n')

    else:
        x=random.randrange(1,5)
        if(x==1):
            print('Desculpa, não entendi o que você falou.\n')
        elif(x==2):
            print('Não entendi o que você me disse.\n')
        elif(x==3):
            print('Pode repetir, em outras palavras, não sei ao certo o que você quis dizer.\n')
        elif(x==4):
            print('Fale algo mais claro para mim.\n')
