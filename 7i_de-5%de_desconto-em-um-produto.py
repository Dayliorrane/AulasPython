# Faça um algorítmo que leia o preço de um produto e mostre
# seu novo preço com 5% de desconto.

#print(100 * 5/100)

p = float(input('Digite o valor do produto: '))
d = p - (p * 5/100)

print('Parabéns! Você acaba de ganhar 5% de desconto! De R${} você só paga R${}'.format(p, d))