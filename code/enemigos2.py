import pygame
import random
import math
import sys
from enum import Enum
from player import Player

class DirectionE(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x,y, mapa):
         # Carga las imágenes de los sprites para cada dirección
        self.images = {
            DirectionE.UP: pygame.image.load("./imagenes/personaje_u.png").convert_alpha(),
            DirectionE.DOWN: pygame.image.load("./imagenes/personaje_d.png").convert_alpha(),
            DirectionE.LEFT: pygame.image.load("./imagenes/personaje_l.png").convert_alpha(),
            DirectionE.RIGHT: pygame.image.load("./imagenes/personaje_r.png").convert_alpha(),
        }

        self.speed = 1
        self.x = x
        self.y = y
        self.direction = DirectionE.DOWN
        self.rect = self.images[self.direction].get_rect()
        self.mapa = mapa
        self.player = Player
        self.health = 100  # Atributo vida
        self.health_font = pygame.font.SysFont('Roboto', 18)
        self.vida = 100
        self.vida_barra = pygame.Surface((50, 5))
        self.vida_barra.fill((255, 0, 0))
        enemy_x = 800
        enemy_y = 200

    velocidad = 2
    def update(self, player, speed):
        dx = player.x - self.x
        dy = player.y - self.y
        distancia = math.sqrt(dx ** 2 + dy ** 2)
        if distancia > 0:
            # Normalizar el vector de dirección
            dx = dx / distancia
            dy = dy / distancia
            
            # Mover el enemigo en la dirección del jugador
            self.x += dx * self.speed 
            self.y += dy * self.speed
            
            # Comprobar colisiones con el mapa
            if self.mapa.check_collision(self.x, self.y):
                self.x -= dx * self.velocidad * speed
                self.y -= dy * self.velocidad * speed

    def move(self, direction):
        # Mueve el jugador en la dirección dada y cambia su imagen
        self.direction = direction
        speed = 1
        if direction == DirectionE.UP:
            self.y -= speed
        elif direction == DirectionE.DOWN:
            self.y += speed
        elif direction == DirectionE.LEFT:
            self.x -= speed
        elif direction == DirectionE.RIGHT:
            self.x += speed

       
    def draw(self, screen):
        # Dibuja el sprite en la pantalla
        screen.blit(self.images[self.direction], (self.x, self.y))


    def is_close_enough(self, player):
        dx = player.x - self.x
        dy = player.y - self.y
        distancia = math.sqrt(dx ** 2 + dy ** 2)
        return distancia <= 5
    
        
    def attack(self, player):
        damage = random.randint(1, 10)
        player.take_damage(damage)
        if self.vida < 0:
            self.vida = 0
        print(f"The enemy attacks and deals {damage} damage.")

    
    def recibir_dano(self, cantidad):
        self.vida -= cantidad
        if self.vida <= 0:
            self.kill()
        self.update_vida_barra()
        
    def draw_barra_vida_enemigo(self, screen):
        # Dibuja la barra de vida
        vida_rect = pygame.Rect(0, 0, int(self.vida * 50 / 100), 5)
        pygame.draw.rect(self.vida_barra, (255, 0, 0), vida_rect)
        screen.blit(self.vida_barra, (self.x, self.y - 10))

          


    