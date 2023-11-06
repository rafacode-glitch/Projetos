import pygame
from pygame.locals import *


# Inicializar Pygame
pygame.init()

# Definir tamanho da tela e criar a tela
tamanho_da_tela = (800, 800)
tela = pygame.display.set_mode(tamanho_da_tela)

# Definir cores
branco = (255, 255, 255)
preto = (0, 0, 0)

# Função para desenhar xadrez


def desenhar_xadrez(tela):
    for linha in range(8):
        for coluna in range(8):
            cor = branco if (linha + coluna) % 2 == 0 else preto
            pygame.draw.rect(tela, cor, pygame.Rect(
                coluna * 100, linha * 100, 100, 100))


# Loop principal do jogo
while True:
    # Limpar a tela
    tela.fill(branco)

    # Verificar eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Desenhar xadrez na tela
    desenhar_xadrez(tela)

    # Atualizar a tela
    pygame.display.update()


def criar_tabuleiro():
    tabuleiro = []
    for i in range(8):
        coluna = []
        for j in range(8):
            coluna.append(None)
        tabuleiro.append(coluna)
    return tabuleiro


def posicao_vazia(tabuleiro, posicao):
    x, y = posicao
    return tabuleiro[x][y] is None
