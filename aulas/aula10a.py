# -*- coding: utf-8 -*-

tempo = int(input('Quantos anos tem o seu carro? '))
if tempo <= 3:
	print('Carro novo')
else:
	print('Carro velho')
print('--FIM--')

print('Carro novo' if tempo <= 3 else 'Carro velho')
print('--FIM--')