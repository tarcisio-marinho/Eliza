#!/bin/bash/env python
# coding=UTF-8
# by Tarcisio marinho
# github.com/tarcisio-marinho
import requests
import json
import os



def onde(palavras):
	tam=len(palavras)
	if(palavras[1] == u'fica' or palavras[1] == u'é' or palavras[1] == u'e'):
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
		if(dicionario['status']=='ZERO_RESULTS'):
			print('Não encontrado ou não existe')
			os.system('espeak -v pt-br -g 4 -a 100 "Não encontrado ou não existe "')
		else:

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
				try:
					print(str(palavras[2])+', '+str(nome))
					print(str(pais)+', '+str(sigla_pais))
					os.system('espeak -v pt-br -g 4 -a 100 "'+str(palavras[2])+' ou '+str(nome)+'"')
					os.system('espeak -v pt-br -g 4 -a 100 " fica no pais '+str(pais)+' e tem a sigla '+str(sigla_pais)+'"')
					if(pais==None):
						print(str(nome))
						print(str(sigla))
				except UnicodeDecodeError:
					print('Erro na codificação, tente usar a sigla')
					os.system('espeak -v pt-br -g 4 -a 100 "Erro na codificação, tente usar a sigla"')

			elif(tam==4):
				try:
					print(str(palavras[2])+' '+ str(palavras[3])+', '+nome)
					print(str(pais)+', '+str(sigla_pais))
					os.system('espeak -v pt-br -g 4 -a 100 "'+str(palavras[2])+' '+str(palavras[3])+' ou '+nome+'"')
					os.system('espeak -v pt-br -g 4 -a 100 " fica no pais '+str(pais)+' e tem a sigla '+str(sigla_pais)+'"')
					if(pais==None):
						print(str(nome))
						print(str(sigla))
				except UnicodeDecodeError:
					print('Erro na codificação, tente usar a sigla\nEx: São paulo -> sp')
					os.system('espeak -v pt-br -g 4 -a 100 "Erro na codificação, tente usar a sigla"')

			elif(tam==5):
				try:
					print(str(palavras[2])+' '+ str(palavras[3])+' ' + str(palavras[4])+ ', ' +str(nome))
					os.system('espeak -v pt-br -g 4 -a 100 "'+str(palavras[2])+' '+str(palavras[3])+' '+palavras[4]+' ou '+nome+'"')
					print(str(pais)+', '+str(sigla_pais))
					os.system('espeak -v pt-br -g 4 -a 100 " fica no pais '+str(pais)+' e tem a sigla '+str(sigla_pais)+'"')
				except UnicodeDecodeError:
					print('Erro na codificação, tente usar a sigla')
					os.system('espeak -v pt-br -g 4 -a 100 "Erro na codificação, tente usar a sigla"')
