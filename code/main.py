import pygame
import os
from mapa import Mapa
from Personaje import Personaje
from settings import Settings
from Proyectil import Proyectil
from pygame.sprite import Group
from enemigos import Enemigo


# Inicializar
pygame.init()

def run_game():
    ai_settings = Settings()
    ventana = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Proyecto PRE")
    imagen_pj = pygame.image.load('personaje_d.png')
    imagen_enemigo = pygame.image.load('enemigo_2.png')

    #crear personaje
    personaje = Personaje(ai_settings, ventana, imagen_pj)
    #creamos proyectiles
    proyectil = Group()
    #creamos enemigos
    enemigo1 = Enemigo(ai_settings, ventana, imagen_enemigo)
    #enemigo1 = Group()

    #reloj = pygame.time.Clock()

    #dibujar mapa
    mapa_partida = Mapa()
    #muros = mapa_partida.construir_mapa(ventana)

    jugando = True
    while jugando:

        #reloj.tick(60)
        #detectar controles jugador
        Personaje.check_events(ai_settings, ventana, personaje, proyectil)
        #actualizamos accion del personaje
        personaje.update()
        #actualizamos proyectiles
        proyectil.update()
        #actualizamos enemigos
        enemigo1.update()

        #dibujar mapa
        #mapa_partida.construir_mapa(ventana)

        #actualizar ventana
        ventana.fill(ai_settings.bg_color)

        #construir mapa
        #mapa.construir_mapa(ventana)

        #redibujar proyectiles
        for bullet in proyectil.sprites():
            bullet.draw_bullet()

        # dibujar personaje
        personaje.blitme()
        # dibujar enemigo
        enemigo1.blitme()

        pygame.display.update()

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