# -*- coding: utf-8 -*-

preco = float(input('Informe o preço do produto: R$'))
novoPreco = preco * 0.95 #preco * (preco do produto - 5%)
print('Preço com desconto: R${:.2f}'.format(novoPreco))