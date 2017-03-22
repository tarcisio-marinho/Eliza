#!/bin/bash
if cd /home/tarcisio/Área\ de\ Trabalho/Musicas/$1 == true
then 
	echo "Digite a música: "
	read entrada
	if ls | grep $entrada
		echo "conseguiu"
	
	else
		echo "nao foi"
	fi
		
else
	echo Artista não encontrado
fi

