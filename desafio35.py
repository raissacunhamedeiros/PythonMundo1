#Desenvolva um programa que leia o comprimento de 3 retas e diga ao usuario
#se elas podem ou não formar um triângulo.
print('-=-' *20)
print("Analisador de Triângulos")
print('-=-' *20)
r1= float(input("Qual tamanho da 1º reta: "))
r2= float(input("qual tamanho da 2º reta: "))
r3= float(input("qual tamanho da 3º reta: "))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("Os segmentos acima podem formar um triângulo")
else:
    print("Os segmentos acima NÃO formam um triângulo")
