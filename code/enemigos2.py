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
        self.remove()

        #imagen Enemigo
        self.image = imagen

        #rect enemigo
        self.rect = self.image.get_rect()
        self.ventana_rect = ventana.get_rect()

        #pos incial enemigo
        self.centerx = float(random.randrange(ai_settings.screen_width))
        self.centery = float(random.randrange(ai_settings.screen_height))
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery

        self.dir = -1
        self.dir2 = -1

        #guardar numero float del centro del enemigo
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

        self.vida = 10

    def update(self):
        self.centerx += self.ai_settings.enemigo_speed_factor*self.dir
        self.rect.centerx = self.centerx
        self.centery += self.ai_settings.enemigo_speed_factor*self.dir2
        self.rect.centery = self.centery

        #limites pantalla y cambio de dirección
        if self.rect.right > self.ai_settings.screen_width:
            self.dir = -1.0
        if self.rect.left < 0:
            self.dir = 1.0
        if self.rect.bottom > self.ai_settings.screen_height:
            self.dir2 = -1.0
        if self.rect.top < 0:
            self.dir2 = 1.0



    # def blitme(self):
    #     #dibuja enemigo en su pos actual
    #     self.ventana.blit(self.image, self.rect)

    def draw_enemigo(self):
        pygame.draw.rect(self.ventana, self.image, self.rect)

    def update_vida(enemigos, ai_settings, proyectil):
        #enemigo.update()
        colision = pygame.sprite.groupcollide(enemigos, proyectil, True, True)

        # for col in colision:
        #     enemigos.vida -= ai_settings.proyectil_dmg
        #
        # if enemigos.vida <= 0:
        #     enemigos.kill()

    def update_enemigos(ai_settings, ventana, enemigo, proyectil):

        enemigo.update()
        #enemigo.update_vida(enemigo, ai_settings, proyectil)
        # if pygame.sprite.spritecollideany(enemigo, proyectil):
