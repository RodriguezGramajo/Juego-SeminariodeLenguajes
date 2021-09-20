import pygame
import random
import os
from pygame.constants import USEREVENT

from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

#inicializo modulos de pygame
pygame.init()
#Seteo la pantalla
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

#Reloj 
clock = pygame.time.Clock()


class Marine(pygame.sprite.Sprite):
    def __init__(self,):
        super(Marine, self).__init__()
        #Cargo imagen para el sprite, cambio el tamaño a 64px 
        marine_sprite = pygame.image.load(os.path.join("sources", "marine.png")).convert()
        self.surf = pygame.transform.scale(marine_sprite,(64,64))
        self.surf.set_colorkey((0,0,0), RLEACCEL)
        self.rect = self.surf.get_rect()

    #Definicion para mover el sprite con el input del usuario, limitado a los bordes de la pantalla    
    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

class Zergling(pygame.sprite.Sprite):
    def __init__(self):
        super(Zergling, self).__init__()
        zergling_sprite = pygame.image.load(os.path.join("sources", "zergling.png")).convert()
        self.surf = pygame.transform.scale(zergling_sprite,(48,48))
        self.surf.set_colorkey((0,0,0), RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )
        self.speed = random.randint(5, 20)

    # Move the sprite based on speed
    # Remove the sprite when it passes the left edge of the screen
    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 250)

#creo al jugador
player = Marine()

#creo grupos de enemigos
enemies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

#run hasta el cierre
running = True
while running:
    #Busco el cierre de ventana
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False

        elif event.type == QUIT:
            running = False
        
        elif event.type == ADDENEMY:
            new_enemy = Zergling()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)


    pressed_keys = pygame.key.get_pressed()

    player.update(pressed_keys)
    enemies.update()

    screen.fill((194,178,128))
#dibujo todo sprite
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)
#check de colision con el jugador
    if pygame.sprite.spritecollideany(player, enemies):
        player.kill
        running = False
    pygame.display.flip()
    #FrameRate: 30 fps
    clock.tick(30)

pygame.quit()
