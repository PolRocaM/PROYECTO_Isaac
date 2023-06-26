import random
import pygame
import math
from enemigo import Enemigo
from Proyectil import *

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

        # parametros vida enemigo
        self.health_font = pygame.font.SysFont('Roboto', 18)
        self.largo = 500
        self.ancho = 25
        self.vida = 500
        # barra de vida total
        self.vida_barra_max = pygame.Surface((self.largo, self.ancho))
        self.vida_barra_max.fill((0, 0, 0))
        self.vida_barra = pygame.Surface((self.vida * 70 / 100, 50))
        self.vida_barra.fill((255, 0, 0))

        self.ai_settings.dmg_enemigo = 25
        self.disparo = 1500
        self.ultimo_disparo = pygame.time.get_ticks()
        self.dx = 0
        self.dy = 0

    def update(self, personaje, enemigo, ai_settings):
        self.dx = personaje.rect.centerx - self.centerx
        self.dy = personaje.rect.centery - self.centery
        distancia = math.sqrt(self.dx ** 2 + self.dy ** 2)
        if distancia > 0:
            # Normalizar el vector de dirección
            self.dx = self.dx / distancia
            self.dy = self.dy / distancia

            # Mover el enemigo en la dirección del jugador
            self.centerx += self.dx * self.ai_settings.boss_speed_factor
            self.centery += self.dy * self.ai_settings.boss_speed_factor
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery


    def draw_barra_vida_enemigo(self):
        calculo_largo = int(self.vida)
        self.vida_barra = pygame.Surface((calculo_largo, self.ancho))
        borde = pygame.Rect(0, 0, self.largo, self.ancho)
        rectangulo = pygame.Rect(0, 0, calculo_largo, self.ancho)
        pygame.draw.rect(self.vida_barra_max, (0, 0, 0), borde)
        pygame.draw.rect(self.vida_barra, (255, 0, 0), rectangulo)
        self.ventana.blit(self.vida_barra_max, (self.ventana_rect.left + 390, self.ventana_rect.bottom - 120))
        self.ventana.blit(self.vida_barra, (self.ventana_rect.left + 390, self.ventana_rect.bottom - 120))
        self.ventana.blit(pygame.image.load('./imagenes/marco_health_boss.png'), (self.ventana_rect.left + 375, self.ventana_rect.bottom - 130))

    def update_barra_vida(self):
        self.vida = self.vida
        self.vida_barra = pygame.Surface((self.vida*200/100, 25))
        self.draw_barra_vida_enemigo()