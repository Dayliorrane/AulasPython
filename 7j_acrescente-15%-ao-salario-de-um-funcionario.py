# Faça um algorítmo que leia o salário de um funcionário e
# mostre seu novo salário com 15% de aumento.

s = float(input('Qual é seu salário atual: R$ '))
# nvs = s + (s * 15/100)
nvs = s * 0.15 + (s)
print('Parabéns! Seu salário passou de R${} para R${}'.format(s, nvs))
