#Faça um programa que leia se o ano é bissexto
from datetime import date
ano = int(input('Digite qual o ano você quer saber se é bissexto, caso queira analisar o ano  atual digite 0:  '))
if ano == 0:
    anor=date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print("O ano {} que você escolheu é bissexto.".format(ano))
else:
    print("Esse ano {} não é bissexto.".format(ano))