import pygame
import sys
from Proyectil import *
from pygame.sprite import Sprite

class Personaje(Sprite):

    def __init__(self, ai_settings, ventana, imagen):
        super(Personaje,self).__init__()
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

        #barra de vida
        self.largo = 200
        self.ancho = 25
        self.health_font = pygame.font.SysFont('Roboto', 18)
        self.vida = 100
        #barra de vida total
        self.vida_barra_max = pygame.Surface((self.largo, self.ancho))
        self.vida_barra_max.fill((0, 0, 0))
        #barra de vida actual
        self.vida_barra = pygame.Surface((int((self.vida/100)*self.largo), self.ancho))
        self.vida_barra.fill((125, 125, 125))

        self.proyectil_up = False
        self.proyectil_down = False
        self.proyectil_right = False
        self.proyectil_left = False
        self.cadencia = 250
        self.ultimo_disparo = pygame.time.get_ticks()

    def update(self, enemigos, ai_settings, ventana, personaje, proyectil):
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

        # Update rect object from self.center.
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery

        #mantener para disparar
        if self.proyectil_up:
            self.image = pygame.image.load('personaje_u.png')
            ahora = pygame.time.get_ticks()
            if ahora-self.ultimo_disparo > self.cadencia:
                Proyectil.fire_bullet(ai_settings, ventana, personaje, proyectil, pygame.K_UP)
                self.ultimo_disparo = ahora
        elif self.proyectil_down:
            self.image = pygame.image.load('personaje_d.png')
            ahora = pygame.time.get_ticks()
            if ahora - self.ultimo_disparo > self.cadencia:
                Proyectil.fire_bullet(ai_settings, ventana, personaje, proyectil, pygame.K_DOWN)
                self.ultimo_disparo = ahora
        elif self.proyectil_left:
            self.image = pygame.image.load('personaje_l.png')
            ahora = pygame.time.get_ticks()
            if ahora - self.ultimo_disparo > self.cadencia:
                Proyectil.fire_bullet(ai_settings, ventana, personaje, proyectil, pygame.K_LEFT)
                self.ultimo_disparo = ahora
        elif self.proyectil_right:
            self.image = pygame.image.load('personaje_r.png')
            ahora = pygame.time.get_ticks()
            if ahora - self.ultimo_disparo > self.cadencia:
                Proyectil.fire_bullet(ai_settings, ventana, personaje, proyectil, pygame.K_RIGHT)
                self.ultimo_disparo = ahora

        self.check_col_enemigo(enemigos)

    def check_col_enemigo(self, enemigos):
        colision_enemigo = pygame.sprite.spritecollide(self, enemigos, False)
        # actualizamos vida personaje
        if colision_enemigo:
            self.vida -= 0.25
            if self.vida <= 0:
                self.vida = 0
                self.kill()

    def draw_barra_vida(self, vida):
        calculo_largo = int((vida/100)*self.largo)
        self.vida_barra = pygame.Surface((calculo_largo, self.ancho))
        borde = pygame.Rect(0, 0, self.largo, self.ancho)
        rectangulo = pygame.Rect(0, 0, calculo_largo, self.ancho)
        pygame.draw.rect(self.vida_barra_max, (0, 0, 0), borde)
        pygame.draw.rect(self.vida_barra, (0, 255, 0), rectangulo)
        self.ventana.blit(self.vida_barra, (self.screen_rect.left+20, self.screen_rect.top+20))
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
            personaje.proyectil_up = True
        if event.key == pygame.K_DOWN:
            personaje.proyectil_down = True
        if event.key == pygame.K_LEFT:
            personaje.proyectil_left = True
        if event.key == pygame.K_RIGHT:
            personaje.proyectil_right = True

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
        if event.key == pygame.K_UP:
            personaje.proyectil_up = False
        elif event.key == pygame.K_DOWN:
            personaje.proyectil_down = False
        if event.key == pygame.K_LEFT:
            personaje.proyectil_left = False
        if event.key == pygame.K_RIGHT:
            personaje.proyectil_right = False

    def check_events(ai_settings, ventana, personaje, proyectil):
        """Respond to keypresses events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                Personaje.check_keydown_events(event, ai_settings, ventana, personaje, proyectil)
            elif event.type == pygame.KEYUP:
                Personaje.check_keyup_events(event, personaje)
