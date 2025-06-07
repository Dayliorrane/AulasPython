# Faça um programa que leia o comprimento do cateto oposto
# e do cateto adjacente de um triângulo retangulo, calcule
# e mostre o comprimento da hipotenusa.
# Para realizar o calculo da hipotenusa, deve-se calcular o 1° cateto ao quadrado
# + o 2° cateto ao quadrado e após isso, realizar o cálculo da raiz do resultado obtido
# na soma dos catetos.

import math

cat_opost = int(input('Digite o valor do cateto oposto: '))
cat_adja = int(input('Digite o valor do cateto adjacente: '))
calc_catetos = cat_opost **2 + cat_adja **2
hipot = math.sqrt(calc_catetos)

print('A hipotenusa é {}'.format(hipot))