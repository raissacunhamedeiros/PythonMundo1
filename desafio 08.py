#escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros
m=float(input('Digite um número em metros:'))
km= m / 1000
hm = m / 100
dam= m / 10
dm= m * 10
cm= m * 100
mm= m * 1000
print('O número em metros é {}\nEquivale a: {} km\n{} hm\n{} dam\n{:.0f}cm\n{:.0f}mm'.format(m,km,hm,dam,dm,cm,mm))

