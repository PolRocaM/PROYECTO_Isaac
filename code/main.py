import sys
import pygame
from Personaje import Personaje
from settings import Settings
from Proyectil import Proyectil
from enemigo import Enemigo
from mapa import Mapa
from nivel import Nivel

# Inicializar
pygame.init()

# matriz_1 = [
#     [1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1],
#     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#     [1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
#     [1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
#     [2, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
#     [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#     [1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
#     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#     [1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1],
# ]

matriz_1 = [
    "1111111111111111",
    "1000000000000001",
    "1000000000000001",
    "1001000000001001",
    "1001000000001001",
    "1001000000001001",
    "1000001111000001",
    "1000000000000001",
    "1111111111111111"
]

def run_game():

    matriz2 = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 3, 0, 0, 5, 0, 0, 1],
        [1, 0, 0, 0, 3, 2, 3, 3, 3, 0, 0, 1],
        [1, 0, 0, 0, 0, 3, 0, 0, 4, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    ]

    reloj = pygame.time.Clock()
    ai_settings = Settings()
    ventana = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Proyecto PRE")

    nivel = Nivel()
    muros = nivel.crearMapa(matriz_1)

    #crear personaje
    personaje = Personaje(ai_settings, ventana)
    #sprites.add(personaje)

    #creamos proyectiles
    proyectil = pygame.sprite.Group()

    # creamos enemigos
    enemigos = pygame.sprite.Group()
    enemigo1 = Enemigo(ai_settings, ventana)
    enemigo2 = Enemigo(ai_settings, ventana)
    enemigo3 = Enemigo(ai_settings, ventana)
    enemigos.add(enemigo1, enemigo2, enemigo3)

    fps = 60
    jugando = True

    while jugando:

        # actualizar ventana
        ventana.fill(ai_settings.bg_color)
        nivel.dibujar_mapa(ventana, muros)

        # mapa.sprites.draw(ventana)

        #detectar controles jugador
        Personaje.check_events(ai_settings, personaje)

        #actualizamos accion del personaje
        personaje.update(enemigos, ai_settings, ventana, personaje, proyectil)

        # GAME OVER
        if personaje.vida == 0:
            jugando = False

        #actualizamos proyectiles
        Proyectil.update_bullets(proyectil, ai_settings, muros)

        #actualizamos enemigos
        #Enemigo.update_enemigos(enemigos, personaje, ai_settings)
        enemigo1.update(personaje, enemigos, ai_settings)
        enemigo1.update_vida(ai_settings, proyectil, enemigos)
        enemigo2.update(personaje, enemigos, ai_settings)
        enemigo2.update_vida(ai_settings, proyectil, enemigos)
        enemigo3.update(personaje, enemigos, ai_settings)
        enemigo3.update_vida(ai_settings, proyectil, enemigos)

        # dibujar personaje
        personaje.blitme()
        personaje.draw_barra_vida(personaje.vida)

        # dibuja enemigos y vida de cada enemigo
        enemigos.draw(ventana)
        Enemigo.update_barra_vida(enemigo1)
        Enemigo.update_barra_vida(enemigo2)
        Enemigo.update_barra_vida(enemigo3)

        proyectil.draw(ventana)
        pygame.display.update()
        # reloj.tick(fps)
        # Make the most recently drawn screen visible.
        pygame.display.flip()

if __name__ == '__main__':

    run_game()

    # Salir
    pygame.quit()
#
# for muro in muros:
#     if personaje.colliderect(muro[0]) and muro[1] == "muro":
#         personaje.x -= personaje_vel_x
#         personaje.y -= personaje.y