#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
#e peça para o usuario tentar descobrir qual foi o número escolhido
#pelo computador. o programa deverá escrever na tela se p user venceu
#ou perdeu
import random
from time import sleep
n = random.randint(0,5)
print('-=-'*20)
print("vou pensar em um número entre 0 e 5. Tente adivinhar...")
print('-=-'*20)
chute = int(input(" Tente acertar o número secreto de 0 a 5: "))
print('PROCESSANDO...')
sleep(3)
if chute == n:
    print("você escolheu o número {}. PARABÉNS você VENCEU!".format(chute))
else:
    print("Infelizmente você perdeu! O número correto era {} e você escolheu o {}.".format(n,chute))