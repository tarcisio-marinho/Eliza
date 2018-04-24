#!/bin/bash/env python
# coding=UTF-8
# by Tarcisio marinho
# github.com/tarcisio-marinho
import json
import requests
import os

def filmes(titulo):
    try:

        req = requests.get('http://www.omdbapi.com/?t='+titulo) #
        dicionario = json.loads(req.text) # converte json em dicionario
        try:
            print('Titulo: '+dicionario['Title'])
            os.system('espeak -v pt-br -g 4 -a 100 " O filme '+dicionario['Title']+'"')
            a = dicionario['Year']
            print('Ano: '+a)
            #os.system('espeak -v pt-br -g 4 -a 100 " Lançado no ano '+a+' "')
            print('Atores: '+dicionario['Actors'])
            os.system('espeak -v pt-br -g 4 -a 100 "Tem os atores principais '+dicionario['Actors']+'"')
            b = dicionario['imdbRating']
            print('Nota IMDB: '+b)
            c = str(b)
            c = c.split('.')
            os.system('espeak -v pt-br -g 4 -a 100 " E teve a nota'+c[0] +' ponto ' + c[1] + ' Segundo o IemeDeBe"')
            print('Poster: '+dicionario['Poster'])
        except KeyError:
            print('Filme não encontrado!\n')
            os.system('espeak -v pt-br -g 4 -a 100 " Filme não encontrado!"')
    except:
        print('Erro na conexão\n')
        os.system('espeak -v pt-br -g 4 -a 100 " Erro na conexão"')


## cotacao do dolar

def cotacao(moeda):
    if(moeda == u'USD'):
        nome_moeda ='dolar'
    elif(moeda == u'BTC'):
        nome_moeda ='bitcoin'
    else:
        nome_moeda ='euro'
    try:
        requisicao = requests.get('http://api.promasters.net.br/cotacao/v1/valores')
        cotacao = json.loads(requisicao.text)
        a = cotacao['valores'][moeda]['valor']
        b = str(a)
        b = b.split('.')
        print('R$ '+ str(a))
        if(nome_moeda != "bitcoin"):
            os.system('espeak -v pt-br -g 4 -a 100 " O valor do '+nome_moeda+' é '+b[0]+'reais e '+b[1]+' centavos"')
        else:
            os.system('espeak -v pt-br -g 4 -a 100 " O valor do '+nome_moeda+' é ' + str(a) + 'reais."')
            
    except:
        print('Erro na conexão\n')
        os.system('espeak -v pt-br -g 4 -a 100 " Erro na conexão"')
