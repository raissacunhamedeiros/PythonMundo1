#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
#para salarios superiores a 1250,00 calcule um aumento de 10%
#para os inferiores ou iguais, o aumento é de 15%
salario = float(input('Escreva seu salário: '))
if salario > 1250.00:
    aumento = salario + (salario*10/100)
    print("Seu salario passará de R${} para R$ {} com 10% de aumento.".format(salario,aumento))
else:
    aumento = salario + (salario * 15 / 100)
    print("Seu salario passará de R${} para R$ {} com 15% de aumento.".format(salario, aumento))