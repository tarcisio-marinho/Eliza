#!/bin/bash/env python
# coding=UTF-8
# by Tarcisio marinho
# github.com/tarcisio-marinho
import os

# pega o nome de todas as musicas #
def listar(diretorio):

    # cria uma lista onde será adicionado o nome da musica #
    musicas = []
    for caminho, diretorio, arquivo in os.walk(diretorio):
        for musica in arquivo:
            if(".mp3" in musica or ".wav" in musica):
                musicas.append(os.path.join(caminho, musica))

    # retorna a lista com todas as musicas #
    return musicas
