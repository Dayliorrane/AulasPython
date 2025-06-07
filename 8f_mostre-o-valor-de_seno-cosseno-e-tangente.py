# Faça um programa que leia um ângulo qualquer e mostre na
# tela o valor do seno, cosseno e tangente desse ângulo.
import math

a = int(input('Digite o ângulo: '))
sen = float(math.sin(math.radians(a)))
cos = float(math.cos(math.radians(a)))
tang = float(math.tan(math.radians(a)))

print('Para o ângulo de {}°, temos o seno  {:.5f}, cosseno {:.5f} e a tangente {:.5f}'.format(a, sen, cos, tang))