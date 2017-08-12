# -*- coding: utf-8 -*-

salario = float(input('Informe o salário: '))

if (salario > 1250):
	salario *= 1.1
else:
	salario *= 1.15

print('Salário com aumento: {:.2f}'.format(salario))