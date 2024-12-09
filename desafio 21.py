#Faça um programa em python que abra e reproduza o aúdio de um arquivo MP3
import math
a = int(input('Digite um número inteiro: '))
b = int(input('Digite um número inteiro: '))
c = int(input('Digite um número inteiro: '))

delta = b**2 - (4*a*c)
print(delta)

if delta <= 0 :
  print('Valor de delta é {}, essa equação não possui raízes reais.'.format(delta))
else:
  raiz = math.sqrt(delta)
  x1= -(b) + raiz/ (a*2)
  x2= -(b) - raiz/ (a*2)
  print('O valor de x1={:.2f} e x2={:.2f}'.format(x1,x2))
