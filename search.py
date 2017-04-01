#!/bin/bash/env python
# coding=UTF-8
# by Tarcisio marinho
# github.com/tarcisio-marinho
import requests
import json
import os

def qual(palavras):
	print(frase)


def onde(palavras):
	tam=len(palavras)
	if(palavras[1]=='fica'):
		try:
			if(tam==3):
				req=requests.get('http://maps.googleapis.com/maps/api/geocode/json?address='+palavras[2])
			elif(tam==4):
				req=requests.get('http://maps.googleapis.com/maps/api/geocode/json?address='+palavras[2]+' '+palavras[3])
			elif(tam==5):
				req=requests.get('http://maps.googleapis.com/maps/api/geocode/json?address='+palavras[2]+' '+palavras[3]+' '+palavras[4])
		except:
			print('Erro de conexão')
			os.system('espeak -v pt-br -g 4 -a 100 " Erro na conexão"')
			return

		dicionario=json.loads(req.text)
		try: # pais
			nome=dicionario['results'][0]['address_components'][0]['long_name']
			sigla=dicionario['results'][0]['address_components'][2]['short_name']
			pais=dicionario['results'][0]['address_components'][3]['long_name']
			sigla_pais=dicionario['results'][0]['address_components'][3]['short_name']

		except IndexError: # estado
			try:
				nome=dicionario['results'][0]['address_components'][0]['long_name']
				sigla=nome=dicionario['results'][0]['address_components'][0]['short_name']
				pais=dicionario['results'][0]['address_components'][1]['long_name']
				sigla_pais=dicionario['results'][0]['address_components'][1]['short_name']
			except IndexError: # país
				nome=dicionario['results'][0]['address_components'][0]['long_name']
				sigla=nome=dicionario['results'][0]['address_components'][0]['short_name']
				pais=None
				sigla_pais=None

		if(tam==3):
			print(str(palavras[2])+', '+str(nome))
			print(str(pais)+', '+str(sigla_pais))
			os.system('espeak -v pt-br -g 4 -a 100 "'+str(palavras[2])+' ou '+str(nome)+'"')
			os.system('espeak -v pt-br -g 4 -a 100 " fica no pais '+str(pais)+' e tem a sigla '+str(sigla_pais)+'"')
			if(pais==None):
				print(str(nome))
				print(str(sigla))

		elif(tam==4):
			print(str(palavras[2])+' '+ str(palavras[3])+', '+nome)
			print(str(pais)+', '+str(sigla_pais))
			os.system('espeak -v pt-br -g 4 -a 100 "'+str(palavras[2])+' '+str(palavras[3])+' ou '+nome+'"')
			os.system('espeak -v pt-br -g 4 -a 100 " fica no pais '+str(pais)+' e tem a sigla '+str(sigla_pais)+'"')
			if(pais==None):
				print(str(nome))
				print(str(sigla))

		elif(tam==5):
			print(str(palavras[2])+' '+ str(palavras[3])+' ' + str(palavras[4])+ ', ' +str(nome))
			print(str(pais)+', '+str(sigla_pais))
