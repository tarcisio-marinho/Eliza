#!/bin/bash/env python
# coding=UTF-8
# by Tarcisio marinho
# github.com/tarcisio-marinho
import os
from socket import *
def conexao():
    # servidor
    meuIP='127.0.0.1'
    porta=6061

    socket_obj = socket(AF_INET, SOCK_STREAM)
    socket_obj.bind((meuIP, porta))
    socket_obj.listen(1) # escuta apenas 1 cliente

    while True:
    	conexao,endereco=socket_obj.accept()
    	print('servidor conectado por', endereco)
        arq=open('conectados.txt','w') #
        arq.write(str(endereco)+'\n') # escreve no arquivo dos hosts conectados
    	# recebe dados enviados pelo cliente
    	while True:

    		data = conexao.recv(1024)
    		conexao.send(b'Eco=>' + data)

    	conexao.close()
conexao()
