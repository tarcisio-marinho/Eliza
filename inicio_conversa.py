#!/bin/usr/env python
import random
class Inicio():
	def __init__(self):
		self.ois=0

	def compara(self,palavras):
		if(palavras[0]=='oi' or palavras[0]=='ola' or palavras[0]=='oie' or palavras[0]=='iae' or palavras[0]=='dale' or palavras[0]=='opa' or palavras[0]=='ooi' or palavras[0]=='oii'):
			x=random.randrange(1,5)
			if(x==1):
				print('Ola')
			elif(x==2):
				print('Oi')
			elif (x==3):
				print('Opa')
			else:
				print('Iae :D')
