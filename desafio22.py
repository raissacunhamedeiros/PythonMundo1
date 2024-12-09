#Crie um programa que leia o nome completo de uma pessoa
#e mostre:
#O nome com todas as letras maiúsculas
#O nome com todas minúsculas
#Quantas letras ao todo sem considerar espaços
#Quantas letras tem o primeiro nome
nome = str(input('Digite seu nome completo: ')).strip()
dividido= nome.split()
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculass é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome)- nome.count(' ')))
print('Seu Primeiro tem {} letras.'.format(nome.find(' ')))
#separa = nome.split()
#print('Seu Primeiro nome é {} tem {} letras.'.format(separa[0], len(separa)))
