# Crie um algorítmo que leia um número e mostre o seu dobro, triplo e raiz quadrada

n1 = int(input('Digite um número: '))
d = n1 * 2
t = n1 * 3
r = n1 ** (1/2)

print('O dobro de {} é {}, o triplo é {} e a raiz quadrada é {}'.format(n1, d, t, r))