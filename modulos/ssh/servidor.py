#!/bin/bash/env python
# coding=UTF-8
# by Tarcisio marinho
# github.com/tarcisio-marinho
import os
from socket import *
from RSA.gera_chaves import *
from RSA.descriptografa import *
def conexao():
    # servidor
    meuIP='127.0.0.1'
    porta=6063

    socket_obj = socket(AF_INET, SOCK_STREAM)
    socket_obj.bind((meuIP, porta))
    socket_obj.listen(1) # escuta apenas 1 cliente

    while True:
    	conexao,endereco=socket_obj.accept()
    	print('servidor conectado por', endereco)
        print('gerando as chaves... ')
        gerador() # gera as chaves e salva nos arquivos
        arquivo1=open('chave_publica.txt','r')
        n=arquivo1.readline()
        n=int(n)
        e=arquivo1.readline()
        e=int(e)
        print(n,e)
        conexao.send(b'' + str(n) +','+ str(e))

        # enviou as chaves publicas

        #try:
        #    arq=open('conectados.txt','a')
        #except:
        #    arq=open('conectados.txt','w') # cria arquivo

        #arq.write(str(endereco)+'\n') # escreve no arquivo dos hosts conectados
    	# recebe dados enviados pelo cliente
    	while True:
    	   recebido = conexao.recv(1024)
           print(recebido)
           recebido.replace(' ','')
           recebido=recebido.split(',')
           print(recebido[0])
           print(type(recebido[0]))
           descriptografado=descifra(recebido,n)
    	   conexao.send(b'texto original: ' + descriptografado)

    	conexao.close()
conexao()
