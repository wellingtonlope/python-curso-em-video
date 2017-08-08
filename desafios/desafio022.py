# -*- coding: utf-8 -*-

nome = input('Digite o seu nome completo: ')
print('Letras maiúsculas: {}'.format(nome.upper()))
print('Letras minúsculas: {}'.format(nome.lower()))
print('Quantidade de letras sem espaços: {}'.format(len(nome.replace(' ', ''))))
nomeS = nome.split()
print('Quantas letras tem o nome: {}'.format(len(nomeS[0])))