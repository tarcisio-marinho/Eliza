#!/bin/bash/env python
# coding=UTF-8
# by Tarcisio marinho
# github.com/tarcisio-marinho
from socket import *
from RSA.criptografa import *

def conecta():
    serverHost='127.0.0.1' # CLIENTE TEM QUE INSERIR O IP DO HOST QUE ELE QUER SE CONECTAR
    porta=6066

    socket_obj = socket(AF_INET, SOCK_STREAM)
    socket_obj.connect((serverHost, porta))


    # chave publica
    data = socket_obj.recv(1024) # recebeu do servidor a chave publica
    chave_publica=data.split(',') # separou a chave -> N e E
    print('Conectado ao servidor\nConexão criptografada\n')

    while True:
        frase=raw_input('client@'+serverHost+':~$ ') # texto a ser criptografado e enviado
        criptografado=cipher(frase,int(chave_publica[0]),int(chave_publica[1])) # criptografou o texto
        string=str(criptografado)
        string=string.replace('[',' ').replace(']',' ').replace(' ','')
        mensagem=b'%s' %(string) # enviou para o servidor em forma de string o texto
        socket_obj.send(mensagem)
        confirmacao=socket_obj.recv(1024)
        if(int(confirmacao)==0):
            print('comando executado')
        else:
            print('Comando incorreto')


conecta()
