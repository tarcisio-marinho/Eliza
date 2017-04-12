#!/bin/bash/env python
# coding=UTF-8
# by Tarcisio marinho
# github.com/tarcisio-marinho
import requests,json,os
def minha_localizacao(frase):
    url='http://freegeoip.net/json/'
    try:
        requisicao=requests.get('http://freegeoip.net/json/')
        dicionario=json.loads(requisicao.text)

        if(frase=='pais'):
            print('Você está no ')
            print(str(dicionario['country_name'])+', '+str(dicionario['country_code']))

        elif(frase=='estado'):
            print('Você está em ')
            print(str(dicionario['city'])+'-'+str(dicionario['region_code'])+', '+dicionario['region_name'])

        elif(frase=='ip'):
            print('Seu ip é: '+str(dicionario['ip']))

    except:
        print('Erro de conexão')
        os.system('espeak -v pt-br -g 4 -a 100 "Erro de conexão"')
