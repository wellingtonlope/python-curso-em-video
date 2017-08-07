# -*- coding: utf-8 -*-

largura = float(input('Informe a largura da parede em metros: '))
altura = float(input('Informe a altura da parede em metros: '))
area = largura * altura
tinta = area / 2
print('Você precisa de {:.2f} litros de tinta'.format(tinta))