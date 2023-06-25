import random
import pygame
from pygame.sprite import Sprite

class Enemigo(Sprite):
    def __init__(self, ai_settings, ventana):
        super(Enemigo, self).__init__()
        self.ventana = ventana
        self.ai_settings = ai_settings

        #imagen Enemigo
        self.image = pygame.image.load('./imagenes/enemigo_2.png')

        #rect enemigo
        self.rect = self.image.get_rect()
        self.ventana_rect = ventana.get_rect()

        #pos incial enemigo
        self.centerx = float(random.randrange(ai_settings.screen_width))
        self.centery = float(random.randrange(ai_settings.screen_height))
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery

        self.dir = -1 #parametro para cambiar la dirección x
        self.dir2 = -1 #parametro para cambiar la dirección y

        #guardar numero float del centro del enemigo
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

        #parametros vida enemigo
        self.health_font = pygame.font.SysFont('Roboto', 18)
        self.vida = 100
        self.vida_barra = pygame.Surface((self.vida*45/100, 5))
        self.vida_barra.fill((255, 0, 0))

    def update(self, personaje, enemigos, ai_settings):
        #moviment enemigo
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
        # if self.rect == personaje.rect.centery-25:
        #     self.dir2 = self.dir2 *-1
        # if self.rect == (personaje.rect.centerx)-25:
        #     self.dir = self.dir*-1
        # self.centery = self.centery
        # self.centerx = self.centerx


    def update_vida(self, ai_settings, proyectil, enemigos, personaje):

        colisiones = pygame.sprite.groupcollide(enemigos, proyectil, False, True)
        for enemigos, proyectiles in colisiones.items():
            # print (enemigos, proyectiles)
            for i in proyectiles:
                enemigos.vida -= ai_settings.proyectil_dmg
                if enemigos.vida <= 0:
                    enemigos.vida = 0
                    enemigos.kill()
                    personaje.dinero += 25
                    print(personaje.dinero)

    def draw_barra_vida_enemigo(self):
        # Dibuja la barra de vida
        vida_rect = pygame.Rect(0, 0, self.vida, 5)
        pygame.draw.rect(self.vida_barra, (255, 0, 0), vida_rect)
        self.ventana.blit(self.vida_barra, (self.rect.left, self.rect.bottom+3))

    def update_barra_vida(enemigo):
        enemigo.vida = enemigo.vida
        enemigo.vida_barra = pygame.Surface((enemigo.vida*45/100, 5))
        enemigo.draw_barra_vida_enemigo()

