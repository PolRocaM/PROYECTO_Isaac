import sys
import pygame
from Personaje import Personaje
from settings import Settings
from Proyectil import Proyectil
from enemigo import Enemigo
from nivel import Nivel
from enemigo_tipo2 import Enemigo_tipo2

# Inicializar
pygame.init()

fuente1 = pygame.font.SysFont("arial black", 24)
fuente2 = pygame.font.SysFont("Segoe print", 32)

matriz_1 = [
    "11111111111111111111111111111111",
    "10000000000000000000000000000001",
    "10000000000000000000000000000001",
    "10000000000000000000000000000001",
    "10000000000000000000000000000001",
    "10000000000000000000000000000001",
    "10000000000000000000000000000001",
    "10000000000000000000000000000001",
    "10000000000000000000000000000002",
    "10000000000000000000000000000002",
    "10000000000000000000000000000001",
    "10000000000000000000000000000001",
    "10000000000000000000000000000001",
    "10000000000000000000000000000001",
    "10000000000000000000000000000001",
    "10000000000000000000000000000001",
    "10000000000000000000000000000001",
    "11111111111111111111111111111111"
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
    next_level = False
    reloj = pygame.time.Clock()
    ai_settings = Settings()
    ventana = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Proyecto PRE")

    nivel = Nivel()
    muros = nivel.crearMapa(matriz_1)

    #crear personaje
    personaje = Personaje(ai_settings, ventana)
    #creamos proyectiles
    proyectil = pygame.sprite.Group()
    # creamos enemigos
    enemigos = pygame.sprite.Group()


    fps = 60
    jugando = True
    menu_principal=True
    nivel_1 = False
    nivel_2 = False

    while jugando:
        # GAME OVER
        if personaje.vida == 0:
            nivel_1 = False
            ventana.fill((0, 0, 0))
            historia = [
                "Has Muerto"
            ]
            y = 100
            for frase in historia:
                texto = fuente2.render(frase, True, (255, 255, 255))
                ventana.blit(texto, (150, y))
                y += 40
            pygame.display.update()
            pygame.time.delay(5000)
            menu_principal = True

        while menu_principal:
            ventana.fill((255, 255, 205))
            historia = [
                "new game <Press enter>",
                "Exit"
            ]
            y = 100
            for frase in historia:
                texto = fuente2.render(frase, True, (0, 0, 0))
                ventana.blit(texto, (150, y))
                y += 40
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    menu_principal = False
                    jugando = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        menu_principal = False
                        ventana.fill((0, 0, 0))
                        historia = [
                            "nivel 1"
                        ]
                        y = 100
                        for frase in historia:
                            texto = fuente2.render(frase, True, (255, 255, 255))
                            ventana.blit(texto, (150, y))
                            y += 40
                        pygame.display.update()
                        pygame.time.delay(3000)
                        enemigo1 = Enemigo(ai_settings, ventana)
                        enemigo2 = Enemigo(ai_settings, ventana)
                        enemigo3 = Enemigo(ai_settings, ventana)
                        enemigos.add(enemigo1, enemigo2, enemigo3)
                        nivel_1 = True

        while nivel_1:
            # actualizar ventana
            ventana.fill(ai_settings.bg_color)
            nivel.dibujar_mapa(ventana, muros)

            # mapa.sprites.draw(ventana)

            #detectar controles jugador
            Personaje.check_events(ai_settings, personaje)

            #actualizamos accion del personaje
            personaje.update(enemigos, ai_settings, ventana, personaje, proyectil, muros)

            #actualizamos proyectiles
            Proyectil.update_bullets(proyectil, ai_settings, muros)

            #actualizamos enemigos
            #Enemigo.update_enemigos(enemigos, personaje, ai_settings)
            enemigo1.update(personaje, enemigos, ai_settings)
            enemigo1.update_vida(ai_settings, proyectil, enemigos, personaje)
            enemigo2.update(personaje, enemigos, ai_settings)
            enemigo2.update_vida(ai_settings, proyectil, enemigos, personaje)
            enemigo3.update(personaje, enemigos, ai_settings)
            enemigo3.update_vida(ai_settings, proyectil, enemigos, personaje)

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

            #transicio a nivel 2
            if len(enemigos) == 0:
                nivel_1 = False
                ventana.fill((0, 0, 0))
                historia = [
                    "Nivel 2"
                ]
                y = 100
                for frase in historia:
                    texto = fuente2.render(frase, True, (255, 255, 255))
                    ventana.blit(texto, (200, y))
                    y += 40
                pygame.display.update()
                pygame.time.delay(3000)
                enemigo4 = Enemigo_tipo2(ai_settings, ventana)
                enemigo5 = Enemigo_tipo2(ai_settings, ventana)
                enemigos.add(enemigo4, enemigo5)
                nivel_2 = True

        while nivel_2:

            # actualizar ventana
            ventana.fill(ai_settings.bg_color)
            nivel.dibujar_mapa(ventana, muros)

            # mapa.sprites.draw(ventana)

            # detectar controles jugador
            Personaje.check_events(ai_settings, personaje)

            # actualizamos accion del personaje
            personaje.update(enemigos, ai_settings, ventana, personaje, proyectil, muros)

            nivel.check_siguiente_nivel(enemigos)

            # actualizamos proyectiles
            Proyectil.update_bullets(proyectil, ai_settings, muros)

            # actualizamos enemigos
            # Enemigo.update_enemigos(enemigos, personaje, ai_settings)
            enemigo4.update(personaje, enemigos, ai_settings)
            enemigo4.update_vida(ai_settings, proyectil, enemigos, personaje)
            enemigo5.update(personaje, enemigos, ai_settings)
            enemigo5.update_vida(ai_settings, proyectil, enemigos, personaje)

            # dibujar personaje
            personaje.blitme()
            personaje.draw_barra_vida(personaje.vida)

            # dibuja enemigos y vida de cada enemigo
            enemigos.draw(ventana)
            Enemigo_tipo2.update_barra_vida(enemigo4)
            Enemigo_tipo2.update_barra_vida(enemigo5)

            proyectil.draw(ventana)
            pygame.display.update()
            # reloj.tick(fps)
            # Make the most recently drawn screen visible.
            pygame.display.flip()

            if len(enemigos) == 0:
                nivel_2 = False
                ventana.fill((0, 0, 0))
                historia = [
                    "Has ganado"
                ]
                y = 100
                for frase in historia:
                    texto = fuente2.render(frase, True, (255, 255, 255))
                    ventana.blit(texto, (200, y))
                    y += 40
                pygame.display.update()
                pygame.time.delay(3000)
                menu_principal = True


if __name__ == '__main__':

    run_game()

    # Salir
    pygame.quit()
