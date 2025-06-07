# Faça um programa que leia um número inteiro e mostre na tela o
# seu sucessor e o seu antecessor.

n1 = int(input('Digite um número: '))
a = n1 - 1
s = n1 + 1

print('O sucessor de {} é {} e o antecessor é {}'.format(n1, s, a))