#Crie um programa que leia um número inteiro qualquer e mostre
#na tela se ele é par ou impar
numero =  int(input("digite um número inteiro: "))
resto = numero % 2
if resto == 0:
    print('O número escolhido {} é par!'.format(numero))
else:
    print("O número escolhido é ímpar!")