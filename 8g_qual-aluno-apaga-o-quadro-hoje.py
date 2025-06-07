# Um professor quer sortear um dos seus 4 alunos para apagar o
# quadro. Faça um programa que ajude ele, lendo o nome deles e
# escrevendo o nome do escolhido.

import random
from time import daylight

print('Olá, professor! Digite o nome dos alunos para o sorteio')
aluno1 = str(input('Digite o nome do 1° aluno(a): '))
aluno2 = str(input('Digite o nome do 2° aluno(a): '))
aluno3 = str(input('Digite o nome do 3° aluno(a): '))
aluno4 = str(input('Digite o nome do 4° aluno(a): '))

alunos = aluno1, aluno2, aluno3, aluno4
sorteado = random.choice(alunos)

print('Parabéns {}! Hoje é você que apaga o quadro!'.format(sorteado))
