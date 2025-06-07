# Crie um programa que leia um número real qualquer pelo teclado e
# mostre na tela a sua porção inteira.
# Ex: Digite um número: 6.127
# O número 6.127 tem a porção inteira 6.
import math

num = float(input('Digite um número real: '))
por_int = math.trunc(num)

print('O número {} tem a porção inteira igual a {}'.format(num, por_int))