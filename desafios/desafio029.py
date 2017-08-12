# -*- coding: utf-8 -*-

velocidade = int(input('Informe a velocidade: '))
if (velocidade > 80):
	print('Você foi multado em: R${:.2f}'.format((velocidade - 80) * 7))
else:
	print('Você está dentro do limite de velocidade :)')