#!/bin/bash/env python
# coding=UTF-8
# by Tarcisio marinho
# github.com/tarcisio-marinho
import os

# pega o nome de todas as musicas #
def listar(diretorio):

    # cria uma lista onde será adicionado o nome da musica #
    musicas=[]
    for caminho, diretorio, arquivo in os.walk(diretorio):
        for musica in arquivo:
            a=caminho+'/'+(musica.replace(" ", "\ ").replace(" (", " \("). replace(")", "\)"))
            musicas.append(a)

    # retorna a lista com todas as musicas #
    return musicas
