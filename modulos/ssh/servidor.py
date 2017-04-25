#!/bin/bash/env python
# coding=UTF-8
# by Tarcisio marinho
# github.com/tarcisio-marinho
import os
import datetime
import time
from socket import *
from RSA.gera_chaves import *
from RSA.descriptografa import *
from RSA.criptografa import *
def conexao():
    # servidor
    meuIP='127.0.0.1' # USUARIO QUE TEM QUE CONFIGURAR O IP -> PRIMEIRA VEZ RODANDO -> IFCONFIG -> INSERIR IP MANUALMENTE
    porta=6065

    socket_obj = socket(AF_INET, SOCK_STREAM)
    socket_obj.bind((meuIP, porta))
    socket_obj.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1) # se der ctrl + c, ele para de escutar na porta
    socket_obj.listen(1) # escuta apenas 1 cliente
    print('Servidor rodando')

    while True:
    	conexao,endereco=socket_obj.accept()
        hora=datetime.datetime.fromtimestamp(int(time.time())).strftime('%Y-%m-%d %H:%M:%S') # hora de conexão -> unix timestamp
    	print('servidor conectado por', endereco,hora)
        print('gerando as chaves... ')
        while True: # TESTE PARA GERAR CHAVES CORRETAS
            try:
                palavra_teste='oi'
                gerador()
                arquivo1=open('chave_publica.txt','r')
                n=arquivo1.readline()
                n=int(n)
                e=arquivo1.readline()
                e=int(e)
                criptografado=cipher(palavra_teste,n,e)
                descriptografado=descifra(criptografado,n)
                novo=str(descriptografado)
                novo=novo.replace(']','').replace('[','').replace("'","").replace(',','').replace(' ','')
                if(novo==palavra_teste): # achou as chaves corretas -> para e vai para a conexão
                    break
                else:
                    continua_while=0
            except ValueError as e:
                print('Erro '+str(e) +'tentando proxima chave')
        # FIM DO TESTE -> achou as chaves corretas

        arquivo1=open('chave_publica.txt','r')
        n=arquivo1.readline()
        n=int(n)
        e=arquivo1.readline()
        e=int(e)
        conexao.send(b'' + str(n) +','+ str(e)) # envia pro cliente a chave publica

        try: # tenta abrir e escrever os clientes que foram conectados
            arq=open('conectados.txt','a')
        except:
            arq=open('conectados.txt','w') # cria arquivo

        arq.write(str(endereco)+' - '+str(hora)+'\n') # escreve no arquivo dos hosts conectados

        # recebe dados enviados pelo cliente
    	while True:
           novo_recebido=[]
    	   recebido = conexao.recv(1024) # recebe o que o cliente mandou
           recebido=recebido.split(',') # separa em uma lista

           for caracter in recebido: # remove o L, que tem no fim dos caracteres
               caracter=caracter.replace('L','')
               novo_recebido.append(caracter) # adiciona na nova lista
           descriptografado=descifra(novo_recebido,n)
           descriptografado=str(descriptografado).replace(']','').replace('[','').replace("'","").replace(',','')
           print(descriptografado) # arrumar -> espaços ---  d e  b o a
           conexao.send('ok') # mandou ok, significa que o comando do cliente foi recebido


    	conexao.close()
conexao()
