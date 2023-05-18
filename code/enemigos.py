import random

import pygame
import os
import sys
from pygame.sprite import Sprite



class Enemigo(Sprite):
    def __init__(self, ai_settings, ventana, imagen):
        super(Enemigo, self).__init__()
        self.ventana = ventana
        self.ai_settings = ai_settings

        #imagen Enemigo
        self.image = imagen

        #rect enemigo
        self.rect = self.image.get_rect()
        self.ventana_rect = ventana.get_rect()

        #pos incial enemigo
        self.rect.centerx = self.ventana_rect.centerx
        self.rect.centery = self.ventana_rect.centery #- random.randrange(ai_settings.screen_height-self.rect.centery)

        self.vel = -1
        self.vel2 = -1

        #guardar num float del centro del enemigo
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)


    def update(self):

        self.rect.centerx += 1*self.vel
        self.rect.centery += self.ai_settings.enemigo_speed_factor*self.vel2

        #limites pantalla y cambio de dirección
        if self.rect.right > self.ai_settings.screen_width:
            self.vel = -1

        if self.rect.left < 0:
            self.vel = 1

        if self.rect.bottom > self.ai_settings.screen_height:
            self.vel2 = -1

        if self.rect.top < 0:
            self.vel2 = 1



    def blitme(self):
        #dibuja enemigo en su pos actual
        self.ventana.blit(self.image, self.rect)

    def draw_enemigo(self):
        pygame.draw.rect(self.ventana, self.image, self.rect)
