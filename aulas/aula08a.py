# -*- coding: utf-8 -*-

from math import sqrt
import random
import emoji

numero = random.randint(1,100)
raiz = sqrt(numero)
print('A raiz quadrada de {} é igual a {:.1f}'.format(numero, raiz), end=' ')
print(emoji.emojize(':sunglasses:', use_aliases=True))