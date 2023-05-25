import pygame
import sys
import math
import mapa
from Proyectil import *
from pygame.sprite import Sprite

class Personaje(Sprite):
    pos_ini_x = 0
    pos_ini_y = 0
    x_pixels = 51
    y_pixels = 87

    vida = 100
    damage = 1
    speed = 0

    def __init__(self, ai_settings, ventana, imagen):
        self.ventana = ventana
        self.ai_settings = ai_settings

        #imagen del personaje y su rect
        self.image = imagen
        self.rect = self.image.get_rect()
        self.screen_rect = ventana.get_rect()

        #pos inicial del personaje en el centro de la pantalla
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

        # Store a decimal value for the ship's center.
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

        # Movement flags.
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        # self.proyectil_up = False
        # self.proyectil_down = False
        # self.proyectil_right = False
        # self.proyectil_left = False


    # def crear_pj(self, pos_ini_x, pos_ini_y, x_pixels, y_pixels, imagen):
    #     personaje = pygame.Rect(pos_ini_x, pos_ini_y, x_pixels, y_pixels)  # pos inicial 640,360, tamany pj 68x104 pixels (tamany sprite)
    #     imagen.pygame.image.load('personaje_d.png')
    #     return personaje

    def update(self):
        # Update the personaje's center value, not the rect.
        #mover personaje DERECHA
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.centerx += self.ai_settings.personaje_speed_factor
            self.image = pygame.image.load('personaje_r.png')
        #mover personaje IZQUIERDA
        if self.moving_left and self.rect.left > 0:
            self.centerx -= self.ai_settings.personaje_speed_factor
            self.image = pygame.image.load('personaje_l.png')
        #mover personaje ABAJO
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.centery += self.ai_settings.personaje_speed_factor
            self.image = pygame.image.load('personaje_d.png')
        #mover personaje ARRIBA
        if self.moving_up and self.rect.top > 0:
            self.centery -= self.ai_settings.personaje_speed_factor
            self.image = pygame.image.load('personaje_u.png')

        # png UP cuando disparo proyectil
        # if self.moving_up == True:
        #     self.image = pygame.image.load('personaje_u.png')
        # if self.moving_down == True:
        #     self.image = pygame.image.load('personaje_d.png')
        # if self.moving_right == True:
        #     self.image = pygame.image.load('personaje_r.png')
        # if self.moving_left == True:
        #     self.image = pygame.image.load('personaje_l.png')

        # Update rect object from self.center.
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery

    def blitme(self):
        #dibuja el personaje en su localización actual
        self.ventana.blit(self.image, self.rect)

    def check_keydown_events(event, ai_settings, screen, personaje, proyectil):
        """Respond to keypresses."""
        if event.key == pygame.K_d:
            personaje.moving_right = True
        elif event.key == pygame.K_a:
            personaje.moving_left = True
        elif event.key == pygame.K_w:
            personaje.moving_up = True
        elif event.key == pygame.K_s:
            personaje.moving_down = True

        if event.key == pygame.K_UP:
            Proyectil.fire_bullet(ai_settings, screen, personaje, proyectil, pygame.K_UP)
            #personaje.proyectil_up = True
        elif event.key == pygame.K_DOWN:
            Proyectil.fire_bullet(ai_settings, screen, personaje, proyectil, pygame.K_DOWN)
            #personaje.proyectil_down = True
        elif event.key == pygame.K_LEFT:
            Proyectil.fire_bullet(ai_settings, screen, personaje, proyectil, pygame.K_LEFT)
            #personaje.proyectil_left = True
        elif event.key == pygame.K_RIGHT:
            Proyectil.fire_bullet(ai_settings, screen, personaje, proyectil, pygame.K_RIGHT)
            #personaje.moving_right = True


    def check_keyup_events(event, personaje):
        """Respond to key releases."""
        if event.key == pygame.K_d:
            personaje.moving_right = False
        elif event.key == pygame.K_a:
            personaje.moving_left = False
        elif event.key == pygame.K_w:
            personaje.moving_up = False
        elif event.key == pygame.K_s:
            personaje.moving_down = False

    def check_events(ai_settings, ventana, personaje, proyectil):
        """Respond to keypresses events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                Personaje.check_keydown_events(event, ai_settings, ventana, personaje, proyectil)
            elif event.type == pygame.KEYUP:
                Personaje.check_keyup_events(event, personaje)

    def check_enemy_collision(self, player_x, player_y, enemy_x, enemy_y, enemy_radius):
        distance = math.sqrt((player_x - enemy_x) ** 2 + (player_y - enemy_y) ** 2)
        if distance <= enemy_radius:
            return True
        else:
            return False
