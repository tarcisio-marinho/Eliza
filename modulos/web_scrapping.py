#!/bin/bash/env python
# coding=UTF-8
# by Tarcisio marinho
# github.com/tarcisio-marinho
import bs4 as bs
import lxml
import requests
import os


def busca(mecanismo,string):
    if(mecanismo=='wikipedia' or mecanismo=='wiki'):
        try:
            texto_html = requests.get('https://pt.wikipedia.org/wiki/'+string)
            bs_obj = bs.BeautifulSoup(texto_html.text, 'lxml') # continua em html porém como objeto bs4
        except requests.exceptions.ConnectionError:
            print('Sem conexão a internet')
            return

        try:
            if(str(bs_obj.p.text[0])+ str(bs_obj.p.text[1])+str(bs_obj.p.text[2])=='A W'):
                print('nao achou')
                return
        except:
            pass

        i=0
        for paragraph in bs_obj.find_all('p'):
            i=i+1
            print(paragraph.text)
            if(i==3):
                break

    elif(mecanismo=='google'):
        texto_html = requests.get('https://www.google.com.br/#q='+string)
        bs_obj = bs.BeautifulSoup(texto_html.text, 'lxml')
        for div in bs_obj.find_all('a'):
            print(div.get('data-href'))

while True:
    pesquisa=raw_input('busca: ')
    busca('google',pesquisa)
# YOUTUBE
#class_="yt-lockup-content"
#<a.title>
# a.data-ytid

#receber sites como entrada, ex
# olx -> procura todos os produtos escolhidos
# mercado livre
# facebook
# yt
# google
# steam
# github
# https://www.youtube.com/watch?v=3xQTJi2tqgk
# https://imasters.com.br/desenvolvimento/aprendendo-sobre-web-scraping-em-python-utilizando-beautifulsoup/?trace=1519021197&source=single
