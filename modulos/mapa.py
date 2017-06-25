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

        if(frase== u'pais'):
            print('Você está no ')
            print(str(dicionario['country_name'])+', '+str(dicionario['country_code']))
            os.system('espeak -v pt-br -g 4 -a 100 "Você está no '+str(dicionario['country_name'])+'"')

        elif(frase== u'estado'):
            print('Você está em ')
            print(str(dicionario['city'])+'-'+str(dicionario['region_code'])+', '+dicionario['region_name'])
            os.system('espeak -v pt-br -g 4 -a 100 "Você está em '+str(dicionario['city'])+'"')

        elif(frase== u'ip'):
            print('Seu ip é: '+str(dicionario['ip']))
            os.system('espeak -v pt-br -g 4 -a 100 "Seu ipê é"')

    except:
        print('Erro de conexão')
        os.system('espeak -v pt-br -g 4 -a 100 "Erro de conexão"')

def clima(cidade):
    url='http://api.openweathermap.org/data/2.5/weather?q='+ cidade + '&APPID=ab6ec687d641ced80cc0c935f9dd8ac9&units=metric'
    try:
        requisicao=requests.get(url)
        dicionario=json.loads(requisicao.text)
        print('A temperatura em '+str(cidade)+' é: ' + str(dicionario['main']['temp'])+ ' graus Celcius')
        os.system('espeak -v pt-br -g 4 -a 100 "A temperatura em '+str(cidade)+' é: ' + str(dicionario['main']['temp'])+ ' graus Celcius'+'"')
        if(dicionario['weather'][0]['main']=='Clear'):
            print('O clima está: Limpo/Aberto')
            os.system('espeak -v pt-br -g 4 -a 100 "O clima está: Limpo e Aberto"')
        elif(dicionario['weather'][0]['main']=='Clouds'):
            print('O clima está: Nebuloso/fechado')
            os.system('espeak -v pt-br -g 4 -a 100 "O clima está: Nebuloso e fechado"')
        elif(dicionario['weather'][0]['main']=='Thunderstorm'):
            print('O clima está muito chuvoso e com tempestade, cuidado pae')
            os.system('espeak -v pt-br -g 4 -a 100 "O clima está muito chuvoso e com tempestade, cuidado pae"')
        else:
            print('O clima está: '+ dicionario['weather'][0]['main'])
            os.system('espeak -v pt-br -g 4 -a 100 "O clima está: '+ dicionario['weather'][0]['main']+'"')
    except:
        print('Erro de conexão')
        os.system('espeak -v pt-br -g 4 -a 100 "Erro de conexão"')
