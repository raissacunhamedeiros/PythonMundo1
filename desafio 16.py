#Crie um programa que leia um número real qualquer pelo teclado e mostre na tela sua porção inteira
#ex: digite um número:6.127
#o número 6.127 tem a parte inteira 6
import math
numero = float(input('Escreva um número: '))
print('O número escolhido foi {} e sua parte inteira é {} .'.format(numero,math.trunc(numero)))