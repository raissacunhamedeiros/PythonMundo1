#Faça um programa que leia o comprimento do cateto oposto
#e do cateto adjacente de um trinangulo retangulo
#calcule e mostre o comprimento da hipotenusa.
import math

cateto1 = float(input('Digite o valor do cateto oposto: '))
cateto2 = float(input('Digite o valor do cateto adjacente: '))
hipotenusa = math.hypot(cateto1,cateto2)
print('O valor da hipotenusa é: {:.2f} .'.format(hipotenusa))