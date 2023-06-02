import pygame
from Personaje import Personaje
from settings import Settings
from Proyectil import Proyectil
from enemigo import Enemigo
from mapa import Mapa

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
    mapa = Mapa(matriz)
    reloj = pygame.time.Clock()
    ai_settings = Settings()
    ventana = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    # Titulo ventana
    pygame.display.set_caption("Proyecto PRE")
    imagen_pj = pygame.image.load('personaje_d.png')
    imagen_enemigo = pygame.image.load('enemigo_2.png')
    imagen_enemigo2 = pygame.image.load('enemigo_3.png')


    speed = 5

    #crear personaje
    personaje = Personaje(ai_settings, ventana, imagen_pj)
    #sprites.add(personaje)
    #creamos proyectiles
    proyectil = pygame.sprite.Group()

    #creamos enemigos
    #enemigo = Enemy(800, 100, mapa)
    # creamos enemigos
    enemigos = pygame.sprite.Group()
    enemigo1 = Enemigo(ai_settings, ventana, imagen_enemigo2)
    enemigo2 = Enemigo(ai_settings, ventana, imagen_enemigo)
    enemigo3 = Enemigo(ai_settings, ventana, imagen_enemigo)
    enemigos.add(enemigo1, enemigo2, enemigo3)

    fps = 60
    jugando = True

    while jugando:

        # actualizar ventana
        ventana.fill(ai_settings.bg_color)
        # mapa.sprites.draw(ventana)

        #detectar controles jugador
        Personaje.check_events(ai_settings, ventana, personaje, proyectil)

        #actualizamos accion del personaje
        personaje.update(enemigos, ai_settings, ventana, personaje, proyectil)

        # GAME OVER
        if personaje.vida == 0:
            jugando = False

        #actualizamos proyectiles
        Proyectil.update_bullets(proyectil, ai_settings)

        #actualizamos enemigos
        #Enemigo.update_enemigos(enemigos, personaje, ai_settings)
        # dibujar enemigo
        enemigo1.update(personaje, enemigos, ai_settings)
        enemigo1.update_vida(enemigo1, ai_settings, proyectil, enemigos)
        enemigo2.update(personaje, enemigos, ai_settings)
        enemigo2.update_vida(enemigo2, ai_settings, proyectil, enemigos)
        enemigo3.update(personaje, enemigos, ai_settings)
        enemigo3.update_vida(enemigo3, ai_settings, proyectil, enemigos)


        #redibujar proyectiles
        for bullet in proyectil.sprites():
            bullet.draw_bullet()

        # dibujar personaje
        personaje.blitme()
        personaje.draw_barra_vida(personaje.vida)

        # dibuja enemigos y vida de cada enemigo

        enemigos.draw(ventana)
        Enemigo.update_barra_vida(enemigo1)
        Enemigo.update_barra_vida(enemigo2)
        Enemigo.update_barra_vida(enemigo3)

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