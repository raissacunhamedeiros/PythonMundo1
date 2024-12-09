#Desenvolva um programa que pergunte a distância de uma viagem em KM.
#Calcule o preço da passagem, cobrando 0,50 por km para viagens de até
#200 km e 0.45 para viagens mais longas
distancia = int(input("Qual a distancia da sua viagem em KM? "))
if distancia <= 200:
    calculo = distancia * 0.5
    print("Essa viagem a passagem custará RS {} .".format(calculo))
else:
    calculo = distancia * 0.45
    print("Essa viagem a passagem custará RS {} .".format(calculo))


#calculo = distancia * (0.5 if distancia <= 200 else 0.45)
