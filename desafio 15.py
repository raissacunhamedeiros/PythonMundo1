#Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias
#pelas quais ele foi alugado. Calcule o preço a pagar, sabendo que
#o carro custa R$ 60 por dia e R$0.15 por km rodado
c= float(input('Digite a quantidade de Km rodados:'))
d= int(input('Digite a quantidade de dias que o carro foi alugado:'))
total= (c*0.15) + (d*60)
print('A quantidade de Km rodados foi {:.2f}Km e o carro passou {} dias alugado, logo o preço final a pagar é de {:.2f}'.format(c,d,total))
