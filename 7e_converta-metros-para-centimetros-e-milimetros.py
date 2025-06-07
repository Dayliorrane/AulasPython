# Escreva um programa que leia um valor em metros e exiba
# convertido em centímetros e milímetros.

metr = float(input('Digite um valor em metros: '))
cent = metr * 100
milim = metr * 1000

print('Em {} metros, há {} centímetros'.format(metr, cent))
print('Em {} metros, há {} milímetros'.format(metr, milim))
