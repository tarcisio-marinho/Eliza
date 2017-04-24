#!/bin/bash/env python
# coding=UTF-8
# by Tarcisio marinho
# github.com/tarcisio-marinho
from socket import *
from RSA.criptografa import *

def conecta():
    serverHost='192.168.15.107'
    
    porta=6062

    socket_obj = socket(AF_INET, SOCK_STREAM)
    try:
        socket_obj.connect((serverHost, porta))
    except socket.error:
        print('Servidor offline\n')

    # chave publica
    data = socket_obj.recv(1024) # recebeu do servidor a chave publica
    chave_publica=data.split(',') # separou a chave -> N e E
    print('Conectado ao servidor\nConexão criptografada\n')

    while True:

        frase=raw_input('Comandos -$ ') # texto a ser criptografado e enviado
        criptografado=cipher(frase,int(chave_publica[0]),int(chave_publica[1])) # criptografou o texto
        string=str(criptografado)
        string=string.replace('[',' ').replace(']',' ').replace(' ','')
        mensagem=b'%s' %(string) # enviou para o servidor em forma de string o texto
        socket_obj.send(mensagem)


conecta()
