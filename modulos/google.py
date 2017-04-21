#!/bin/bash/env python
# coding=UTF-8
# by Tarcisio marinho
# github.com/tarcisio-marinho
import requests

def googlis():
    url='https://www.youtube.com/results?search_query='
    busca=raw_input('oq vc quer buscar no yt: ')
    requisicao=requests.get(url+busca)
    print(requisicao.text)
googlis()
