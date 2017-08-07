# -*- coding: utf-8 -*-

algo = input("Digite algo: ")
print("Tipo primitivo {}".format(type(algo)))
print("Contém só números: {}".format(algo.isnumeric()))
print("Contém só letras: {}".format(algo.isalpha()))
print("Contém letras ou números: {}".format(algo.isalnum()))
print("Contém apenas letras maiúsculas: {}".format(algo.isupper()))
print("Contém apenas letras minúsculas: {}".format(algo.islower()))