import  random
import pygame
import math
from enemigo import Enemigo

class Enemigo_Boss(Enemigo):
    def __init__(self, ai_settings, ventana):
        super(Enemigo_Boss, self).__init__(ai_settings, ventana)

        self.ventana = ventana
        self.ai_settings = ai_settings

        self.image = pygame.image.load("./imagenes/boss2.png")
        self.rect = self.image.get_rect()
        self.ventana_rect = ventana.get_rect()

        #pos inicial
        self.centerx = self.ventana_rect.centerx
        self.centery = self.ventana_rect.centery
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery

        self.teleport = 1500
        self.ultimo_teleport = pygame.time.get_ticks()

        self.vida = 500

    def update(self, personaje, enemigos, ai_settings):
        dx = personaje.rect.centerx - self.centerx
        dy = personaje.rect.centery - self.centery
        distancia = math.sqrt(dx ** 2 + dy ** 2)
        if distancia > 0:
            # Normalizar el vector de dirección
            dx = dx / distancia
            dy = dy / distancia

            # Mover el enemigo en la dirección del jugador
            self.centerx += dx * self.ai_settings.boss_speed_factor
            self.centery += dy * self.ai_settings.boss_speed_factor
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery
        # ahora = pygame.time.get_ticks()
        # if ahora - self.ultimo_teleport > self.teleport:
        #     self.centerx = 80 + float(random.randrange(500))
        #     self.centery = 80 + float(random.randrange(500))
        #     self.rect.centerx = self.centerx
        #     self.rect.centery = self.centery
        #     self.ultimo_teleport = ahora