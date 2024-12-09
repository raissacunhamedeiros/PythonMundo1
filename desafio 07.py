#desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média
nota1= float(input('Digite sua primeira nota:'))
nota2= float(input('Digite sua segunda nota:'))
media= (nota1+nota2)/2
print('Sua primeira nota foi {:.1f}, sua segunda nota foi {:.1f} e sua média é {:.1f}'.format(nota1, nota2, media))