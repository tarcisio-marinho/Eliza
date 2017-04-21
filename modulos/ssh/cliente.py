#!/usr/bin/env python
# by Tarcisio Marinho
# github.com/tarcisio-marinho
from socket import *

serverHost='127.0.0.1'
porta=6061

socket_obj = socket(AF_INET, SOCK_STREAM)
socket_obj.connect((serverHost, porta))

while True:
    a = raw_input('Voce: ')
    mensagem = b'%s' % (a)
    socket_obj.send(mensagem)
    data = socket_obj.recv(1024)
    print('cliente recebeu',data)
