# -*- coding: utf-8 -*-

from random import randint

numero = randint(0, 5)
tentativa = int(input('Digite o número que eu pensei: '))
if (numero == tentativa):
	print('Parabéns você acertou :) ')
	print('Computador: {}'.format(numero))
	print('Você: {}'.format(tentativa))
else:
	print('Você errou :(')
	print('Computador: {}'.format(numero))
	print('Você: {}'.format(tentativa))