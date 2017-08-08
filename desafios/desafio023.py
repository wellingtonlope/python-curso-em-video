# -*- coding: utf-8 -*-

numero = input('Digite um número: ')

if(len(numero) == 4):
	print('unidade: {}'.format(numero[3]))
	print('dezena: {}'.format(numero[2]))
	print('centena: {}'.format(numero[1]))
	print('milhar: {}'.format(numero[0]))
elif(len(numero) == 3):
	print('unidade: {}'.format(numero[2]))
	print('dezena: {}'.format(numero[1]))
	print('centena: {}'.format(numero[0]))
elif(len(numero) == 2):
	print('unidade: {}'.format(numero[1]))
	print('dezena: {}'.format(numero[0]))
else:
	print('unidade: {}'.format(numero[0]))