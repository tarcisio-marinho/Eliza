#!/bin/bash/env python
# coding=UTF-8
# by Tarcisio marinho
# github.com/tarcisio-marinho
import json
import requests


def filmes(titulo):
    try:

        req=requests.get('http://www.omdbapi.com/?t='+titulo) #
        dicionario=json.loads(req.text) # converte json em dicionario
        try:
            print('Titulo: '+dicionario['Title'])
            print('Ano: '+dicionario['Year'])
            print('Atores: '+dicionario['Actors'])
            print('Nota IMDB: '+dicionario['imdbRating'])
            print('Poster: '+dicionario['Poster'])
        except KeyError:
            print('Filme não encontrado!\n')
    except:
        print('Erro na conexão\n')


## cotacao do dolar

def cotacao(moeda):
    try:
        requisicao = requests.get('http://api.promasters.net.br/cotacao/v1/valores')
        cotacao = json.loads(requisicao.text)
        print(cotacao['valores'][moeda]['valor']) # imprime o dolar
    except:
        print('Erro na conexão\n')
