# -*- coding: utf-8 -*-

distancia = int(input('Informa a distância: '))
if (distancia <= 200):
	print('Preço: R${:.2f}'.format(distancia * 0.50))
else:
	print('Preço: R${:.2f}'.format(distancia * 0.45))