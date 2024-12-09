# crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode
# comprar. (considere US$1,00= 3,27)
c= float(input('Digite quantos reais você quer converter:R$'))
d= float(input('Digite a cotação atual do Dolar: U$'))
dolar= c/d
euro= c/5.37
print('Com R$ {} reais você obterá U$ {:.2f} dolares ou EUR {:.2f}.'.format(c,dolar,euro))