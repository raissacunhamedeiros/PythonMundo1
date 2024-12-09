#Faça um algoritmo que leia o preço do produto e o novo preço é 5%
preço= float(input('Qual o preço do produto:'))
novo= preço - (preço * 5 / 100)
print('O preço que custava {:.2f}, na promoção o produto sairá por R${:.2f}'.format(preço,novo))
