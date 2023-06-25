import random
import pygame
from enemigo import Enemigo

class Enemigo_tipo2(Enemigo):
    def __init__(self, ai_settings, ventana):
        super(Enemigo_tipo2, self).__init__(ai_settings, ventana)

        self.ventana = ventana
        self.ai_settings = ai_settings

        self.image = pygame.image.load("./imagenes/enemigo_3.png")
        self.rect = self.image.get_rect()
        self.ventana_rect = ventana.get_rect()

        self.centerx = 80 + float(random.randrange(ai_settings.screen_width-160))
        self.centery = 80 + float(random.randrange(ai_settings.screen_height-160))
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery

        self.teleport = random.randrange(1000, 2000)
        self.ultimo_teleport = pygame.time.get_ticks()
        self.sonido_tp = pygame.mixer.Sound('./audio/game-teleport-90735.mp3')
        pygame.mixer.Sound.set_volume(self.sonido_tp, 0.1)

        self.vida = 150

    def update(self, personaje, enemigos, ai_settings):
        ahora = pygame.time.get_ticks()
        if ahora - self.ultimo_teleport > self.teleport:
            self.sonido_tp.play()
            self.centerx = 80 + float(random.randrange(500))
            self.centery = 80 + float(random.randrange(500))
            self.rect.centerx = self.centerx
            self.rect.centery = self.centery
            self.ultimo_teleport = ahora

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