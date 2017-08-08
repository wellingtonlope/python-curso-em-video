# -*- coding: utf-8 -*-

cidade = input('Digite o nome da sua cidade: ')
if ('SANTO' in cidade[:6].upper()):
	print('Começa com SANTO a cidade {}'.format(cidade.upper()))
else:
	print('Não Começa com SANTO a cidade {}'.format(cidade.upper()))