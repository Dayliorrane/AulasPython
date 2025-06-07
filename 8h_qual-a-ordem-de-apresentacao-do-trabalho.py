# O mesmo professor do desafio anterior(019), quer sortear a ordem
# de apresentação de trabalhos dos alunos. faça um programa que leia
# o nome dos quatro alunos e mostre a ordem sorteada.
import random

nome1 = str(input('Digite o nome do primeiro aluno(a): '))
nome2 = str(input('Digite o nome do segundo aluno(a): '))
nome3 = str(input('Digite o nome do terceiro aluno(a): '))
nome4 = str(input('Digite o nome do quarto aluno(a): '))

alunos = nome1, nome2, nome3, nome4

lista = random.sample(alunos, 4)

print('O trabalho deverá ser apresentado na seguinte ordem: \n{}'.format(lista))


