# -*- coding: utf-8 -*-

from math import hypot

oposto = float(input('Informe o cateto oposto: '))
adjacente = float(input('Informe o cateto adjacente: '))
hipotenusa = hypot(oposto, adjacente)
print('Comprimento da Hipotenusa: {:.2f}'.format(hipotenusa))