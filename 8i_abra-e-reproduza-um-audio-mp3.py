# Faça um programa em python que abra e reproduza o áudio
# de um arquivo mp3.

import pygame
# inicializa mixer do pygame
pygame.mixer.init()

# carrega o arquivo mp3
pygame.mixer.music.load("aud2.mp3")

# reproduz o arquivo
pygame.mixer.music.play()

input()
# mantém o programa ativo enquanto a música toca
pygame.mixer.quit()