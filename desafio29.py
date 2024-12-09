#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar
#80 km/hr mostre uma mensagem dizendo que ele foi multado. A multa vai custa
#7,00 por casa km acima do limite
velocidade= int(input("Qual a velocidade do carro? "))
if velocidade > 80:
    calculo = velocidade - 80
    multa = calculo * 7.0
    print("Você foi multado e deverá pagar R$ {} .".format(multa))
else:
    print("Continue dirigindo com segurança!")