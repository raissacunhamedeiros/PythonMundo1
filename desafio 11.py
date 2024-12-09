#faça um programa que leia a largura e a altura de uma parede em metros,
#calcule a sua area e a quantidade de tinta necessária para pinta-la, sabendo
#que cada litro de tinta pinta uma area de 2m²
l=float(input('Quanto de largura a parede tem em metros?'))
a=float(input('Quanto de altura a parede tem em metros?'))
area=l*a
tinta= area/2
print('Sua parede tem a dimensão de {}x{} e sua area é de {} m².\nPara pintar essa parede é necessário {} litros de tinta'.format(l,a,area,tinta,))
