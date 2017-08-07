# -*- coding: utf-8 -*-

nome = input('Qual é o seu nome? ')
#{:>20} alinhado a direita/ {:<20} alinhado a esquerda/ {:^20} alinhado ao meio/ {:=^20} alinhado no meio com espaços
print('Prazer em te conhecer {}!'.format(nome))

n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}, o produto é {} e a divisão é {:.3f}'.format(s, m, d), end=' >>> ')
print('Divisão inteira {} e potência {}'.format(di, e))