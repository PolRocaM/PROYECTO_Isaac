import  random
import pygame
from pygame.sprite import Sprite
from enemigo import Enemigo

class Enemigo_tipo2(Enemigo):
    def __init__(self, ai_settings, ventana):
        super(Enemigo_tipo2, self).__init__(ai_settings, ventana)

        self.ventana = ventana
        self.ai_settings = ai_settings

        self.image = pygame.image.load("personaje_d.png")
        self.rect = self.image.get_rect()
        self.ventana_rect = ventana.get_rect()

        self.centerx = float(random.randrange(ai_settings.screen_width))
        self.centery = float(random.randrange(ai_settings.screen_height))
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery

        self.teleport = 5000
        self.ultimo_teleport = pygame.time.get_ticks()

    def update(self, personaje, enemigos, ai_settings):
        ahora = pygame.time.get_ticks()
        if ahora - self.ultimo_teleport > self.teleport:
            self.centerx = float(random.randrange(ai_settings.screen_width))
            self.centery = float(random.randrange(ai_settings.screen_height))
            self.rect.centerx = self.centerx
            self.rect.centery = self.centery
            self.ultimo_teleport = ahora