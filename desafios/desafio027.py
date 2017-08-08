# -*- coding: utf-8 -*-

nome = input('Digite o seu nome: ')
nomeL = nome.split()
print('Primeiro nome: {}'.format(nomeL[0]))
print('Último nome: {}'.format(nomeL[len(nomeL) - 1]))