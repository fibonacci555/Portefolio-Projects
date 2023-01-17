import pygame
from pygame.locals import *
import random

altura = 800
largura = 1200
moves = 0
max = 0

altura_min = 100
altura_max = 700
largura_min = 100
largura_max = 700

tela = pygame.display.set_mode((largura , altura))

tamanho_pixel = 20
velocidade = 20


def distance(b1,b2):
    d = (((b2.pos[ 0 ] - b1.pos[ 0 ]) ** 2) + ((b2.pos[ 1 ] - b1.pos[ 1 ]) ** 2)) ** (1 / 2)
    return d//20


def warning(snake,apple):
    maior_state = ""
    maior_dist = 0
    if len(snake.bodies) > 4:
        if snake.state == "LEFT":
            for body in snake.bodies:
                if body.pos[0] == snake.pos[0]:
                    if abs(body.pos[1] - snake.pos[1] ) > max:
                        if 0>body.pos[1] - snake.pos[1] :
                            if abs(body.pos[1] - snake.pos[1] )>maior_dist :
                                maior_state = "UP"
                        if body.pos[1] - snake.pos[1] > 0:
                            if abs(body.pos[1] - snake.pos[1] )>maior_dist :
                                maior_state = "DOWN"
                if body.pos[1] == snake.pos[1]:
                    if abs(body.pos[ 0 ] - snake.pos[ 0 ]) > maior_dist:
                        maior_state = "LEFT"
            print(maior_state)
            if maior_state != "":
                snake.state = maior_state





        if snake.state == "RIGHT":
            for body in snake.bodies:
                if body.pos[0] == snake.pos[0]:
                    if abs(body.pos[1] - snake.pos[1] ) > max:
                        if 0>body.pos[1] - snake.pos[1] :
                            if abs(body.pos[1] - snake.pos[1] )>maior_dist :
                                maior_state = "UP"
                        if body.pos[1] - snake.pos[1] > 0:
                            if abs(body.pos[1] - snake.pos[1] )>maior_dist :
                                maior_state = "DOWN"
                if body.pos[1] == snake.pos[1]:
                    if abs(body.pos[ 0 ] - snake.pos[ 0 ]) > maior_dist:
                        maior_state = "RIGHT"
            print(maior_state)
            if maior_state != "":
                snake.state = maior_state







        if snake.state == "UP":
            for body in snake.bodies:
                if body.pos[1] == snake.pos[1]:
                    if abs(body.pos[0] - snake.pos[0] ) > max:
                        if 0>body.pos[0] - snake.pos[0] :
                            if abs(body.pos[0] - snake.pos[0] )>maior_dist :
                                maior_state = "LEFT"
                        if body.pos[0] - snake.pos[0] > 0:
                            if abs(body.pos[0] - snake.pos[0] )>maior_dist :
                                maior_state = "RIGHT"
                if body.pos[0] == snake.pos[0]:
                    if abs(body.pos[ 1] - snake.pos[ 1 ]) > maior_dist:
                        maior_state = "UP"
            print(maior_state)
            if maior_state != "":
                snake.state = maior_state





        if snake.state == "DOWN":
            for body in snake.bodies:
                if body.pos[1] == snake.pos[1]:
                    if abs(body.pos[0] - snake.pos[0] ) > max:
                        if 0>body.pos[0] - snake.pos[0] :
                            if abs(body.pos[0] - snake.pos[0] )>maior_dist :
                                maior_state = "LEFT"
                        if body.pos[0] - snake.pos[0] > 0:
                            if abs(body.pos[0] - snake.pos[0] )>maior_dist :
                                maior_state = "RIGHT"
                if body.pos[0] == snake.pos[0]:
                    if abs(body.pos[ 1] - snake.pos[ 1 ]) > maior_dist:
                        maior_state = "DOWN"
            print(maior_state)
            if maior_state != "":
                snake.state = maior_state



class Apple:
    def __init__( self ):
        self.pos = [ random.randrange(100 , 700 , tamanho_pixel) , random.randrange(100 , 700 , tamanho_pixel) ]

    def new( self ):
        self.pos = [ random.randrange(100 , 700 , tamanho_pixel) , random.randrange(100 , 700 , tamanho_pixel) ]

    def draw( self , surf ):
        pygame.draw.rect(surf , (255 , 200 , 0) , (
            self.pos[ 0 ] + tamanho_pixel // 4 , self.pos[ 1 ] + tamanho_pixel // 4 , tamanho_pixel // 2 ,
            tamanho_pixel // 2))
class snake:
    global moves

    def __init__( self ):
        self.pontos = 0
        self.pos = [ 100 , 100 ]
        self.state = "STOP"
        self.bodies = [ ]
        self.barreiras = False

    def move( self ):
        if self.state == "RIGHT":
            self.pos[ 0 ] += tamanho_pixel
        if self.state == "LEFT":
            self.pos[ 0 ] -= tamanho_pixel
        if self.state == "UP":
            self.pos[ 1 ] -= tamanho_pixel
        if self.state == "DOWN":
            self.pos[ 1 ] += tamanho_pixel
        if self.state == "STOP":
            snake.pontos = -8
            self.pos = self.pos
            for body in self.bodies:
                body.pos = body.pos

    def draw( self , surf ):
        pygame.draw.rect(surf , (0 , 200 , 100) , (self.pos[ 0 ] , self.pos[ 1 ] , tamanho_pixel , tamanho_pixel))
        if len(self.bodies) > 0:
            for i in range(0 , len(self.bodies)):
                if i == 0:
                    self.bodies[ i ].draw(surf , i)
                else:
                    self.bodies[ i ].draw(surf , i)

    def move_body( self ):
        if len(self.bodies) > 0:
            try:
                for i in range(len(self.bodies) - 1 , -1 , -1):
                    if i == 0:

                        self.bodies[ 0 ].pos[ 0 ] = self.pos[ 0 ]
                        self.bodies[ 0 ].pos[ 1 ] = self.pos[ 1 ]
                    else:
                        self.bodies[ i ].pos[ 0 ] = self.bodies[ i - 1 ].pos[ 0 ]
                        self.bodies[ i ].pos[ 1 ] = self.bodies[ i - 1 ].pos[ 1 ]
                    if i > 0:
                        if self.bodies[ i ].pos == self.pos:
                            snake.restart()
            except:
                snake.restart()

    def restart( self ):
        self.pontos = 0
        self.tamanho = 1
        self.pos = [ 400 , 400 ]
        self.state = "STOP"
        self.bodies = [ ]

    def barreira( self ):
        if self.barreiras == True:
            if self.pos[ 0 ] >= largura_max - tamanho_pixel + 1:
                snake.restart()
            if largura_min - 1 >= self.pos[ 0 ]:
                snake.restart()
            if self.pos[ 1 ] >= altura_max - tamanho_pixel + 1:
                snake.restart()
            if largura_min - 1 > self.pos[ 1 ]:
                snake.restart()
        if self.barreiras == False:
            if self.pos[ 0 ] > largura_max - tamanho_pixel + 1:
                snake.pos[ 0 ] = largura_min
            if largura_min - 1 > self.pos[ 0 ]:
                self.pos[ 0 ] = largura_max - 20
            if self.pos[ 1 ] > altura_max - tamanho_pixel + 1:
                self.pos[ 1 ] = altura_min
            if largura_min - 1 > self.pos[ 1 ]:
                self.pos[ 1 ] = altura_max - 20
class body:
    def __init__( self , posX , posY ):
        self.pos = [ posX , posY ]
        self.bodies = [ ]

    def draw( self , surf , a ):
        if a != 0:
            pygame.draw.rect(surf , (random.randint(50 , 255) , random.randint(50 , 255) , random.randint(50 , 255)) ,
                             (self.pos[ 0 ] , self.pos[ 1 ] , tamanho_pixel , tamanho_pixel))
        else:
            pygame.draw.rect(surf , (0 , 200 , 0) , (self.pos[ 0 ] , self.pos[ 1 ] , tamanho_pixel , tamanho_pixel))


def direita( snake ):
    if snake.state != "LEFT":
        snake.state = "RIGHT"
def cima( snake ):
    if snake.state != "DOWN":
        snake.state = "UP"
def baixo( snake ):
    if snake.state != "UP":
        snake.state = "DOWN"
def esquerda( snake ):
    if snake.state != "RIGHT":
        snake.state = "LEFT"


apple = Apple()
snake = snake()

pygame.init()
tamanho = 0
tamanho_max = 0
clock = pygame.time.Clock()


def main():
    global tamanho_max
    global tamanho
    global moves
    global max
    while True:
        tela.fill((0 , 0 , 0))


        if snake.pontos > max:
            max = snake.pontos
        if tamanho > tamanho_max:
            tamanho_max = tamanho

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                break
        """
            if event.type == pygame.KEYDOWN:
                if event.key == K_UP:
                    if snake.state != "DOWN":
                        snake.state = "UP"
                        moves += 1
                if event.key == K_DOWN:
                    if snake.state != "UP":
                        snake.state = "DOWN"
                        moves += 1
                if event.key == K_LEFT:
                    if snake.state != "RIGHT":
                        snake.state = "LEFT"
                        moves += 1
                if event.key == K_RIGHT:
                    if snake.state != "LEFT":
                        snake.state = "RIGHT"
                        moves += 1"""

        if pygame.key.get_pressed()[ K_b ]:
            snake.barreiras = not snake.barreiras

        if pygame.key.get_pressed()[ K_r ]:
            snake.restart()

        if pygame.key.get_pressed()[ K_PLUS ]:
            a = body(snake.pos[ 0 ] , snake.pos[ 1 ])
            tamanho += 1
            snake.bodies.append(a)

        apple.draw(tela)
        snake.draw(tela)
        snake.move()
        snake.barreira()
        snake.move_body()
        right = pygame.draw.line(tela , (255 , 0 , 0) , (largura - 500 , 100) , (largura - 500 , altura - 100))
        left = pygame.draw.line(tela , (255 , 0 , 0) , (100 , 100) , (100 , altura - 100))
        up = pygame.draw.line(tela , (255 , 0 , 0) , (100 , 100) , (largura - 500 , 100))
        down = pygame.draw.line(tela , (255 , 0 , 0) , (100 , altura - 100) , (largura - 500 , altura - 100))

        for x in range(100 , 701 , tamanho_pixel):
            for y in range(100 , 701 , tamanho_pixel):
                pygame.draw.line(tela , (255 , 0 , 0) , (x , y) , (x , altura - y))  # vertical
                pygame.draw.line(tela , (255 , 0 , 0) , (x , altura - y) , (largura - 500 , altura - y))  # horizontal

        if snake.pos == apple.pos:
            tamanho += 1
            a = body(snake.pos[ 0 ] , snake.pos[ 1 ])
            apple.new()
            snake.bodies.append(a)
            snake.pontos += 500
        warning(snake,apple)
        if apple.pos[ 0 ] > snake.pos[ 0 ]:
            direita(snake)
        if snake.pos[ 0 ] > apple.pos[ 0 ]:
            esquerda(snake)
        if apple.pos[ 1 ] > snake.pos[ 1 ]:
            baixo(snake)
        if snake.pos[ 1 ] > apple.pos[ 1 ]:
            cima(snake)
        warning(snake,apple)

        try:
            dt = 1 / clock.get_fps()
            snake.pontos = snake.pontos + dt * 100
        except:
            pass

        fonte = pygame.font.SysFont('arial' , 20 , True , False)
        titulo = pygame.font.SysFont('arial' , 70 , True , True)

        if 30 > snake.pontos:
            moves = 0
            tamanho = 0


        pontos = f"Pontos: {int(snake.pontos)}"
        pontos_format = fonte.render(pontos , True , (255 , 255 , 255))
        tela.blit(pontos_format , (750 , 200))

        tamanho_g = f"Tamanho: {int(tamanho)}"
        tamanho_format = fonte.render(tamanho_g , True , (255 , 255 , 255))
        tela.blit(tamanho_format , (750 , 250))

        moves_p = f"Movimentos: {int(moves)}"
        moves_format = fonte.render(moves_p , True , (255 , 255 , 255))
        tela.blit(moves_format , (750 , 300))

        max_act = f"Máximo: {int(max)}"
        max_act_format = fonte.render(max_act , True , (255 , 255 , 255))
        tela.blit(max_act_format , (750 , 350))

        tamanho_act = f"Tamanho máximo: {int(tamanho_max)}"
        tamanho_act_format = fonte.render(tamanho_act , True , (255 , 255 , 255))
        tela.blit(tamanho_act_format , (750 , 400))

        restart_format = fonte.render("PRESS R TO RESTART" , True , (255 , 255 , 255))
        tela.blit(restart_format , (750 , 600))

        snake_format = titulo.render("S N A K E" , True , (255 , 255 , 255))
        tela.blit(snake_format , (240 , 20))

        clock.tick(velocidade)
        pygame.display.update()



main()
