# -*- coding: utf-8 -*-

from random import shuffle

alunos = []
alunos.append(input('Primeiro aluno: '))
alunos.append(input('Segundo aluno: '))
alunos.append(input('Teceiro aluno: '))
alunos.append(input('Quarto aluno: '))

shuffle(alunos)
print('A ordem de apresentação será ')
print(alunos)