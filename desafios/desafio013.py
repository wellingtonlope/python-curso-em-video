# -*- coding: utf-8 -*-

salario = float(input('Informe o salário do funcionário: R$'))
novoSalario = salario * 1.15 #salario * (salario + 15%)
print('Salário com aumento de 15%: R${:.2f}'.format(novoSalario))