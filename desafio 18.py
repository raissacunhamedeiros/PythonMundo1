#Faça um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente
import math
ang = float(input('Digite o ângulo que você deseja: '))
seno = math.sin(math.radians(ang))
cosseno = math.cos(math.radians(ang))
tangente = math.tan(math.radians(ang))
print('O ângulo de {} tem o seno: {:.2f} , cosseno: {:.2f} e tangente: {:.2f}'.format(ang,seno,cosseno,tangente))