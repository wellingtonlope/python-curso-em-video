# -*- coding: utf-8 -*-

numero = []
numero.append(input('Primeiro número: '))
numero.append(input('Segundo número: '))
numero.append(input('Terceiro número: '))
numero.sort()
print('O maior número é o {}'.format(numero[2]))
print('O menor número é o {}'.format(numero[0]))