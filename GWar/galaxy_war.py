import pygame
import random
from pygame.locals import *
from sys import exit
largura = 1200
altura = 700





red = (255,0,0)
green = (0,255,0)
blue = (0,0,70)
white = (255,255,255)
black = (0,0,0)
orange = (255,140,0)

x_stars = []
y_stars = []


pygame.init()
tela = pygame.display.set_mode((largura,altura))
bg = pygame.image.load("img/bg.jpeg")
nave_img = pygame.image.load("img/nave.png").convert_alpha()
nave_img = pygame.transform.scale(nave_img, (8*20, 7*20))

enemy_img = pygame.image.load("img/enemy.png").convert_alpha()
enemy_img = pygame.transform.scale(enemy_img, (8*20, 7*20))

bala_img = pygame.image.load("img/bala.png").convert_alpha()

bala_inimigo_img = pygame.image.load("img/bala_inimigo.png").convert_alpha()

class Nave():
    def __init__(self):
        self.x = largura//3
        self.y = altura//4
        self.vida = 100

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getVida(self):
        return self.vida

    def restart(self):
        self.x = largura // 3
        self.y = altura // 4
        self.vida = 100

    def hit(self):
        self.vida = self.vida - 10

    def changeX(self,x):
        self.x = self.x + x

    def changeY(self,y):
        self.y = self.y + y

class Inimigo():

    def __init__(self,vel):
        self.x = random.randint(20,largura-20)
        self.y = 0
        self.vida = 2
        self.vel = vel

    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def move(self):
        self.y = self.y + self.vel
    def hit(self):
        self.vida = self.vida - 1
    def setX(self,x):
        self.x = x
    def setY(self,y):
        self.y=y

class Bala():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.vel = 1
        self.exist = False

    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def move(self):
        if self.exist == True:
            self.y = self.y - self.vel

class Bala_inimigo():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vel = 1
        self.exist = False

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def move(self):
        if self.exist == True:
            self.y = self.y + self.vel

class Explosion(pygame.sprite.Sprite):
    def __init__(self, x, y, size):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        for num in range(1, 6):
            img = pygame.image.load(f"img/exp{num}.png")
            if size == 1:
                img = pygame.transform.scale(img, (20, 20))
            if size == 2:
                img = pygame.transform.scale(img, (40, 40))
            if size == 3:
                img = pygame.transform.scale(img, (160, 160))
            #add the image to the list
            self.images.append(img)
            print(num)
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.counter = 0


    def update(self):
        explosion_speed = 3
        #update explosion animation
        self.counter += 1

        if self.counter >= explosion_speed and self.index < len(self.images) - 1:
            self.counter = 0
            self.index += 1
            self.image = self.images[self.index]

        #if the animation is complete, delete explosion
        if self.index >= len(self.images) - 1 and self.counter >= explosion_speed:
            self.kill()

i = 0
vel_bg = 2
vel_enemy = 0.5
disparo = False
explosion_group = pygame.sprite.Group()
l = 1
player = Nave()
enemy1 = Inimigo(vel_enemy)
enemy2 = Inimigo(vel_enemy)
enemy3 = Inimigo(vel_enemy)
enemy4 = Inimigo(vel_enemy)
enemy5 = Inimigo(vel_enemy)

def hit(enemy):
    if player.getX()+50 >= enemy.getX() >=player.getX() and player.getY()+50 >= enemy.getY() >= player.getY():
        return True

def enemy_work(enemy):
    enemy.move()
    tela.blit(enemy_img, (enemy.getX(), enemy.getY()))

pontos = 0
tiro = Bala(player.getX(), player.getY())
enemy_bullet = Bala_inimigo(enemy1.getX(),enemy1.getY())
while True:
    fonte = pygame.font.SysFont('arial', 20, True, False)
    fonte2 = pygame.font.SysFont('G7 Star Force TTF', 137,True, False)
    tela.blit(bg, (0, -altura - i))
    tela.blit(bg, (0, - i))
    if (i == -altura):
        tela.blit(bg, (0, -i))
        i = 0
    i -= 1 / vel_bg
    #tela.fill(black)


    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                tiro.exist = True
                disparo = not disparo

            if event.key == pygame.K_r:
                pontos = 0
                player.vida = 100
                l = 1

            if event.key == pygame.K_g:
                player.vida = player.vida - 5
    if player.vida >= 0:
        if pygame.key.get_pressed()[K_w] or pygame.key.get_pressed()[K_UP]:
            player.changeY(-1.2)
        if pygame.key.get_pressed()[K_s] or pygame.key.get_pressed()[K_DOWN]:
            player.changeY(1.2)
        if pygame.key.get_pressed()[K_a] or pygame.key.get_pressed()[K_LEFT]:
            player.changeX(-1.2)
        if pygame.key.get_pressed()[K_d] or pygame.key.get_pressed()[K_RIGHT]:
            player.changeX(1.2)


    z = 40
    if (enemy1.getX()+z > tiro.getX() > enemy1.getX()-z) and (enemy1.getY()+z >= tiro.getY() >= enemy1.getY()-z):
        explosion = Explosion(enemy1.getX(), enemy1.getY(), 1)
        explosion.update()
        enemy1.x = 10000
        enemy1.y = altura - 20
        pontos = pontos + 1
        disparo = False

    if (enemy2.getX()+z > tiro.getX() > enemy2.getX()-z) and (enemy2.getY()+z >= tiro.getY() >= enemy2.getY()-z):
        explosion = Explosion(enemy2.getX(), enemy2.getY(), 1)
        explosion.update()
        enemy2.x = 10000
        enemy2.y = altura - 20
        pontos = pontos + 1
        disparo = False


    if (enemy3.getX()+z > tiro.getX() > enemy3.getX()-z) and (enemy3.getY()+z >= tiro.getY() >= enemy3.getY()-z):
        explosion = Explosion(enemy3.getX(), enemy3.getY(), 1)
        explosion.update()
        enemy3.x = 10000
        enemy3.y = altura - 20
        pontos = pontos + 1
        disparo = False
        Explosion(enemy1.getX(), enemy1.getY(), 1)


    if (enemy4.getX()+z > tiro.getX() > enemy4.getX()-z) and (enemy4.getY()+z >= tiro.getY() >= enemy4.getY()-z):
        explosion = Explosion(enemy4.getX(), enemy4.getY(), 1)
        explosion.update()
        enemy4.x = 10000
        enemy4.y = altura - 20
        pontos = pontos + 1
        disparo = False

    if (enemy5.getX()+z > tiro.getX() > enemy5.getX()-z) and (enemy5.getY()+z >= tiro.getY() >= enemy5.getY()-z):
        explosion = Explosion(enemy5.getX(), enemy5.getY(), 1)
        explosion.update()
        enemy5.x = 10000
        enemy5.y = altura - 20
        pontos = pontos + 1
        disparo = False

    tela.blit(bala_img,(tiro.getX()+65,tiro.getY()))
    tela.blit(nave_img, (player.getX(), player.getY()))


    if disparo == False:
        tiro.x = player.getX()
        tiro.y = player.getY() + 70

    if disparo == True:
        tiro.move()
    if 0 >=tiro.getY():
        disparo = False
        tiro = Bala(player.getX(), player.getY())

    if l == 1:
        enemy_work(enemy1)
        if enemy1.getY() >= altura:
            l = l + 1
            enemy1.setY(-30)
            enemy1.setX(random.randint(100,largura-100))


    if l == 2:
        enemy_work(enemy2)
        if enemy2.getY() >= altura:
            l = l + 1
            enemy2.setY(-30)
            enemy2.setX(random.randint(100, largura - 100))
    if l == 3:
        enemy_work(enemy3)
        if enemy3.getY() >= altura:
            l = l + 1
            enemy3.setY(-30)
            enemy3.setX(random.randint(100, largura - 100))
    if l == 4:
        enemy_work(enemy4)
        if enemy4.getY() >= altura:
            l = l + 1
            enemy4.setY(-30)
            enemy4.setX(random.randint(100, largura - 100))
    if l == 5:
        enemy_work(enemy5)
        if enemy5.getY() >= altura:
            l = l + 1
            enemy5.setY(-30)
            enemy5.setX(random.randint(100, largura - 100))
    if l > 5:
        l = 1

    if hit(enemy1) or hit(enemy2) or hit(enemy3) or hit(enemy4) or hit(enemy5):
        l_antigo = 0
        if l != l_antigo:
            player.vida = player.vida - 0.3
        l_antigo = l

    explosion_group.draw(tela)
    vida_verm = pygame.draw.rect(tela,red,(player.getX()-20, player.getY()+180, 200,5))
    vida_verde = pygame.draw.rect(tela,green,(player.getX()-20, player.getY()+180, player.vida*2,5))
    vida_txt = fonte.render(str(round(player.vida,0)), True, white)
    pontos_txt = fonte.render(str(pontos), True, white)
    tela.blit(vida_txt,(player.getX()+220, player.getY()+180))
    tela.blit(pontos_txt,(100, altura -100))
    tela.blit(bala_inimigo_img, (enemy_bullet.getX(), enemy_bullet.getY()))


    if 0 >= player.vida:
        restart = "PRESS R TO RESTART"
        restart_txt = fonte2.render(restart,True,white,black)
        tela.blit(restart_txt,(0,altura//2))


    pygame.display.update()



