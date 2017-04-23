#!/usr/bin/env python
# by Tarcisio Marinho
# github.com/tarcisio-marinho
from socket import *
from RSA.criptografa import *

serverHost='127.0.0.1'
porta=6061

socket_obj = socket(AF_INET, SOCK_STREAM)
socket_obj.connect((serverHost, porta))

# chave publica
data = socket_obj.recv(1024) # recebeu do servidor a chave publica
chave_publica=data.split(',') # separou a chave -> N e E
print(chave_publica)

while True:

    frase=raw_input('->') # texto a ser criptografado e enviado
    criptografado=cipher(frase,int(chave_publica[0]),int(chave_publica[1])) # criptografou o texto
    print(criptografado)
    string=str(criptografado)
    string=string.replace('[',' ').replace(']',' ').replace(' ','')
    mensagem=b'%s' %(string) # enviou para o servidor em forma de string o texto
    socket_obj.send(mensagem)

    #a = raw_input('Voce: ')
    #mensagem = b'%s' % (a)
    #socket_obj.send(mensagem)
