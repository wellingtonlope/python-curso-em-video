# -*- coding: utf-8 -*-

frase = input('Digite uma frase: ')
print('Aparece a letra A {} vezes'.format(frase.upper().count('A')))
print('Posição da primeira letra A: {}'.format(frase.upper().find('A')))
print('Posição da última letra A: {}'.format(frase.upper().rfind('A')))