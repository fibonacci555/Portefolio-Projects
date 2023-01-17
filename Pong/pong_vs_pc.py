import pygame
from pygame.locals import *
from sys import exit
from random import randint
import time

pygame.init()

# 0--------------100
# Muito          Muito
# Facil          Dificil

dificuldade = 90

velocidade_bola = 10

velocidade_pongs = 6





largura = 1280
altura = 800

branco = (255, 255, 255)
BLACK = (0, 0, 0)
azul = (0, 0, 255)
vermelho = (255, 0, 0)
pontos_esquerda = 0
pontos_direita = 0
relogio = pygame.time.Clock()
tela = pygame.display.set_mode((largura, altura))
toques = 0



x_esquerda = 0
y_esquerda = 0

x_direita = largura - 20
y_direita = 0

x_bola = randint(300, 600)
y_bola = randint(200, 600)
vel_bola = [velocidade_bola, randint(-7, 7)]




def update():
    global x_bola
    global y_bola
    x_bola = x_bola + vel_bola[0]
    y_bola = y_bola + vel_bola[1]


def rematch():
    bounce()


def bounce():
    vel_bola[0] = -vel_bola[0]
    vel_bola[1] = -randint(-7, 7)


def bounce_bordas():
    vel_bola[1] = -vel_bola[1]


clock = pygame.time.Clock()
bola1 = 0
bola2 = 0

decidido = False
while True:
    if not decidido:
        decisao = randint(0, 100)
        decidido = True
    bola1 = vel_bola[0]
    bola2 = vel_bola[1]
    if 0 > bola1:
        bola1 = -bola1
    if 0 > bola2:
        bola2 = -bola2

    velocidade_bola = bola1 + bola2
    tela.fill(BLACK)
    clock.tick(120)
    printtoques = f"Toques: {toques}"
    pontosdireita = f"PC: {pontos_direita}"
    pontosesquerda = f"Player 1: {pontos_esquerda}"
    velocidadebola = f"Vel Bola: {velocidade_bola}"
    velocidadepongs = f"Vel Pongs: {velocidade_pongs}"
    dificuldade_jogo = f"Dificuldade: {dificuldade // 10}"
    fonte = pygame.font.SysFont('arial', 20, True, False)
    texto_formatado_direita = fonte.render(pontosdireita, True, (255, 255, 255))
    texto_formatado_esquerda = fonte.render(pontosesquerda, True, (255, 255, 255))
    texto_formatado_vel_bola = fonte.render(velocidadebola, True, branco)
    texto_formatado_vel_pongs = fonte.render(velocidadepongs, True, branco)
    texto_formatado_toques = fonte.render(printtoques, True, branco)
    texto_formatado_dificuldade = fonte.render(dificuldade_jogo, True, (255, 255, 255))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    if pygame.key.get_pressed()[K_w]:
        y_esquerda = y_esquerda - velocidade_pongs
    if pygame.key.get_pressed()[K_s]:
        y_esquerda = y_esquerda + velocidade_pongs

    pong_esquerda = pygame.draw.rect(tela, azul, (x_esquerda, y_esquerda, 20, 100))
    pong_direita = pygame.draw.rect(tela, azul, (x_direita, y_direita, 20, 100))
    borda_esquerda = pygame.draw.rect(tela, vermelho, (0, 0, 1, largura))
    borda_direita = pygame.draw.rect(tela, vermelho, ((largura - 1), 0, 1, largura))
    borda_cima = pygame.draw.rect(tela, vermelho, (0, 0, largura, 1))
    borda_baixo = pygame.draw.rect(tela, vermelho, (0, (altura - 1), largura, 1))
    bola = pygame.draw.circle(tela, branco, (x_bola, y_bola), 10)
    if decisao >= 100 - dificuldade:
        if y_direita != y_bola:
            if y_bola > y_direita:
                 y_direita = y_direita + velocidade_pongs
            if y_direita > y_bola:
                y_direita = y_direita - velocidade_pongs
    if 100 - dificuldade > decisao:
        if y_direita != y_bola:
            if y_bola > y_direita:
                y_direita = y_direita + velocidade_pongs
            if y_direita > y_bola:
                y_direita = y_direita - velocidade_pongs

    if bola.colliderect(pong_esquerda) or bola.colliderect(pong_direita):
        bounce()
        toques = toques + 1
        decidido = False
    if bola.colliderect(borda_baixo) or bola.colliderect(borda_cima):  # colisao bordas cima e baixo
        bounce_bordas()

    if x_bola > largura:
        toques = 0
        x_bola = largura // 2
        y_bola = altura // 2
        time.sleep(0.4)
        pontos_esquerda = pontos_esquerda + 1
        decidido = False
    if 0 > x_bola:
        toques = 0
        x_bola = largura // 2
        y_bola = altura // 2
        time.sleep(0.4)
        decidido = False
        pontos_direita = pontos_direita + 1
    tela.blit(texto_formatado_direita, (710, 20))
    tela.blit(texto_formatado_esquerda, (100, 20))
    tela.blit(texto_formatado_vel_bola, (400, 20))
    tela.blit(texto_formatado_vel_pongs, (400, 40))
    tela.blit(texto_formatado_toques, (400, 60))
    tela.blit(texto_formatado_dificuldade, (largura // 1.5, altura - 100))

    update()

    pygame.display.update()
