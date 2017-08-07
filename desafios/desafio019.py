# -*- coding: utf-8 -*-

from random import choice

alunos = []
alunos.append(input('Informe o primeiro aluno: '))
alunos.append(input('Informe o segundo aluno: '))
alunos.append(input('Informe o terceiro aluno: '))
alunos.append(input('Informe o quarto aluno: '))

escolhido = choice(alunos)

print('O {} foi o sorteado'.format(escolhido))