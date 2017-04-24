#!/bin/bash/env python
# coding=UTF-8
# by Tarcisio marinho
# github.com/tarcisio-marinho
from socket import *
from RSA.criptografa import *

def conecta():
    serverHost='192.168.3.199'
    porta=6062

    socket_obj = socket(AF_INET, SOCK_STREAM)
    socket_obj.connect((serverHost, porta))


    # chave publica
    data = socket_obj.recv(1024) # recebeu do servidor a chave publica
    chave_publica=data.split(',') # separou a chave -> N e E
    a=0 # primeira mensagem a ser enviada para o servidor
    print('Conectado ao servidor\nConexão criptografada\n')

    while True:
        if(a==0): # primeira mensagem a ser enviada para testar
            criptografado=cipher('o',int(chave_publica[0]),int(chave_publica[1]))
            print(criptografado) # envia o 'o' para o servidor para testar criptografia
            string=str(criptografado)
            string=string.replace('[',' ').replace(']',' ').replace(' ','')
            mensagem=b'%s' %(string) # enviou para o servidor em forma de string o texto
            socket_obj.send(mensagem)

            a=1

        frase=raw_input('Comandos: -$ ') # texto a ser criptografado e enviado
        criptografado=cipher(frase,int(chave_publica[0]),int(chave_publica[1])) # criptografou o texto
        string=str(criptografado)
        string=string.replace('[',' ').replace(']',' ').replace(' ','')
        mensagem=b'%s' %(string) # enviou para o servidor em forma de string o texto
        socket_obj.send(mensagem)
        confirmacao=socket_obj.recv(1024)
        if(confirmacao=='ok'):
            a=1
            # continua mandando msgs
        else:
            print('servidor offline, conexão encerrada')
            exit()


conecta()
