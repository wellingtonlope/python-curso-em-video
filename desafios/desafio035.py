# -*- coding: utf-8 -*-

r1 = float(input('Primeira reta: '))
r2 = float(input('Segunda reta: '))
r3 = float(input('Terceira reta: '))

if (abs(r2 - r3) < r1 and r1 < r2 + r3) and (abs(r1 - r3) < r2 and r2 < r1 + r3) and (abs(r1 - r2) < r3 and r3 < r1 + r2):
	print('Forma triângulo')
else:
	print('Não forma triângulo')