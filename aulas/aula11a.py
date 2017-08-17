# -*- coding: utf-8 -*-

#style 0=none 1=bold 4=underline 7=negative
#text 30=branco 31=vermelho 32=verde 33=amarelo 34=margenta 35=roxo 36=ciano 37=cinza
#back 40=branco 41=vermelho 42=verde 43=amarelo 44=margenta 45=roxo 46=ciano 47=cinza

print("\033[0;30;41m Teste \033[m")
print("\033[4;33;44m Teste \033[m")
print("\033[1;35;43m Teste \033[m")
print("\033[30;42m Teste \033[m")
print("\033[m Teste ")
print("\033[7;30m Teste \033[m")

nome = "Wellington"
cores = {'limpa':'\033[m', 'azul':'\033[34m', 'amarelo':'\033[33m', 'pretoebranco':'\033[7;30m'}
print("Olá, {}{}{}".format(cores['azul'], nome, cores['limpa']))