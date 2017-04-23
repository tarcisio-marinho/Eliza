#!/bin/bash/env python
# coding=UTF-8
# by Tarcisio marinho
# github.com/tarcisio-marinho

from descriptografa import *

def mod(a,b): # mod function
    if(a<b):
        return a
    else:
        c=a%b
        return c

def cipher(words,e,n): # get the words and compute the cipher
    tam=len(words)
    i=0
    lista=[]
    while(i<tam):
        letter=words[i]
        k=ord(letter)
        k=k**e
        d=mod(k,n)
        lista.append(d)
        i=i+1
    return lista


arquivo1=open('chave_publica.txt','r')
n=arquivo1.readline()
n=int(n)
e=arquivo1.readline()
e=int(e)
texto_puro=raw_input('insira o texto: ')
resp=cipher(texto_puro,e,n)

texto=descifra(resp,n)
print(texto)
