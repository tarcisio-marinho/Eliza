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
    meuIP='192.168.3.199' # ip estatico - corrigir
    porta=6062

    socket_obj = socket(AF_INET, SOCK_STREAM)
    socket_obj.bind((meuIP, porta))
    socket_obj.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1) # se der ctrl + c, ele para de escutar na porta
    socket_obj.listen(1) # escuta apenas 1 cliente
    print('Servidor rodando')

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



        try:
            arq=open('conectados.txt','a')
        except:
            arq=open('conectados.txt','w') # cria arquivo

        arq.write(str(endereco)+'\n') # escreve no arquivo dos hosts conectados

        # recebe dados enviados pelo cliente
    	while True:
           novo_recebido=[]
    	   recebido = conexao.recv(1024) # recebe o que o cliente mandou
           recebido=recebido.split(',') # separa em uma lista

           for caracter in recebido: # remove o L, que tem no fim dos caracteres
               caracter=caracter.replace('L','')
               novo_recebido.append(caracter) # adiciona na nova lista
           descriptografado=descifra(novo_recebido,n)
           print(str(descriptografado))
           conexao.send('ok') # mandou ok, significa que o comando do cliente foi recebido

           #teste
           char = str(descriptografado[0])
           print(char)
           # validações
           #if():
               #conexao.close()

    	conexao.close()
conexao()
