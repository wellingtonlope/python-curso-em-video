# -*- coding: utf-8 -*-

from math import sin, cos, tan, radians
angulo = float(input('Informe o ângulo: '))
radiano = radians(angulo)
print('Seno: {:.3f}'.format(sin(radiano)))
print('Consseno: {:.3f}'.format(cos(radiano)))
print('Tangente: {:.3f}'.format(tan(radiano)))