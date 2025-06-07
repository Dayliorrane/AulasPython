# Crie um programa que leia a altura e a largura de uma parede
# em metros, calcule sua área e a quantidade de tinta necessária
# para pintá-la , sabendo que cada litro de tinta pinta uma área de 2m².

alt = float(input('Digite a altura: '))
larg = float(input('Ok, agora digite a largura: '))
a = larg * alt
tinta = a / 2

print('A área total é {} m²'.format(a))
print('E para {} m² serão necessários {} litros de tinta'.format(a, tinta))