#Faça um programa que leia uma frase pelo teclado e mostre:
#Quantas vezes aparece a letra A / Em que posição ela aparece a 1 vez/
#Em que posição ela aparece a ultima vez:
frase = str(input("Escreva uma frase: ")).strip()
print('A letra A aparece {} vezes na frase.'.format(frase.upper().count('A')))
print('A primeira letra A aparece na posição {}.'.format(frase.find('A')+1))
print('A última letra A apareceu na posição {}.'.format(frase.rfind('A')+1))