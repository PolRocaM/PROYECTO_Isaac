import pygame
import os
import math
from Personaje import Personaje
from settings import Settings
from Proyectil import Proyectil
from pygame.sprite import Group
from enemigos import Enemy
from enemigos2 import Enemigo
from mapa import Mapa
import random

# Inicializar
pygame.init()

def run_game():
    # Crea el objeto del mapa
    matriz = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    ]
    matriz2 = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    ]
    #mapa = Mapa(matriz)
    ai_settings = Settings()
    ventana = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    # Titulo ventana
    pygame.display.set_caption("Proyecto PRE")
    imagen_pj = pygame.image.load('personaje_d.png')
    imagen_enemigo = pygame.image.load('enemigo_2.png')
    speed = 5

    #crear personaje
    personaje = Personaje(ai_settings, ventana, imagen_pj)
    #sprites.add(personaje)
    #creamos proyectiles
    proyectil = pygame.sprite.Group()

    #creamos enemigos
    #enemigo = Enemy(800, 100, mapa)

    enemigos = pygame.sprite.Group()
    enemigo1 = Enemigo(ai_settings, ventana, imagen_enemigo)
    enemigos.add(enemigo1)

    fps = 60
    reloj = pygame.time.Clock()
    jugando = True

    while jugando:

        #reloj.tick(60)
        #detectar controles jugador
        Personaje.check_events(ai_settings, ventana, personaje, proyectil)
        #actualizamos accion del personaje
        personaje.update()
        #actualizamos proyectiles
        Proyectil.update_bullets(proyectil, ai_settings, enemigos)
        #actualizamos enemigos
        #enemigo.update(personaje, speed)
        Enemigo.update_enemigos(ai_settings, ventana, enemigos, proyectil)
        Enemigo.update_vida(enemigos, ai_settings, proyectil)

        #actualizar ventana
        ventana.fill(ai_settings.bg_color)
        #mapa.sprites.draw(ventana)
        #enemigo.draw_barra_vida_enemigo(ventana)

        #redibujar proyectiles
        for bullet in proyectil.sprites():
            bullet.draw_bullet()

        # dibujar personaje
        personaje.blitme()
        # dibujar enemigo
        enemigos.draw(ventana)

        pygame.display.update()
        #reloj.tick(fps)
        # Make the most recently drawn screen visible.
        #pygame.display.flip()

run_game()

# Salir
pygame.quit()
#
# for muro in muros:
#     if personaje.colliderect(muro[0]) and muro[1] == "muro":
#         personaje.x -= personaje_vel_x
#         personaje.y -= personaje.y