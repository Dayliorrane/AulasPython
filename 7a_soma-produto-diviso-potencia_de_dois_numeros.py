# Faça um programa que mostre a soma, o produto, a divisão,
# a divisão inteira e a potência de dois valores

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

print('Soma {} \nProduto {} \nDivisão {:.3f}'.format(s, m, d), end= ' ')
print('\nDivisão inteira {} \nPotência {}'.format(di, e))