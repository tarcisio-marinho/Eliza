#!/bin/bash/env python
# coding=UTF-8
# by Tarcisio marinho
# github.com/tarcisio-marinho
import bs4 as bs
import lxml
import requests
import os


def busca(string):
    try:
        texto_html = requests.get('https://pt.wikipedia.org/wiki/'+string)
        bs_obj = bs.BeautifulSoup(texto_html.text, 'lxml') # continua em html porém como objeto bs4
    except requests.exceptions.ConnectionError:
        print('Sem conexão a internet')
        os.system('espeak -v pt-br -g 4 -a 100 "Sem conexão com a internet"')
        return

    try:
        if(str(bs_obj.p.text[0])+ str(bs_obj.p.text[1])+str(bs_obj.p.text[2])=='A W'):
            print('nao achou')
            os.system('espeak -v pt-br -g 4 -a 100 "Não achou"')
            return
    except:
        pass

    i=0
    for paragraph in bs_obj.find_all('p'):
        i+=1
        print(paragraph.text)
        if(i == 3):
            break
