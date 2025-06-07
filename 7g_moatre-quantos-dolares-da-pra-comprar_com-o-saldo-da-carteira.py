# Crie um programa que leia quanto dinheiro uma pessoa tem na
# carteira e mostre quantos dólares ela pode comprar.
# Considere a cotação de $1 = R$3,27

saldo = float(input('Quanto você tem na carteira? '))

tot_compra = saldo / 3.27

print('Você pode comprar {:.3f} dólares'.format(tot_compra))
