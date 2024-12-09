#faça um algoritmo que leia o salario de um funcionário e mostre seu novo salario com 15% de aumento
s=float(input('Qual seu salario?'))
aumento= s + (s*15/100)
print('O funcionário que ganhava R$ {} , passará a ganhar com 15% de aumento um salario de R${:.2f}'.format(s,aumento))
