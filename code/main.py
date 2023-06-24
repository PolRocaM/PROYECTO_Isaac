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
    "11111111111111122111111111111111",
    "10000000000000000000000000000001",
    "10000000000000000000000000000001",
    "10000000000000000000000000000001",
    "10000000000000000000000000000001",
    "10000000000000000000000000000001",
    "10000000000000000000000000000001",
    "10000000000000000000000000000001",
    "10000000000000000000000000000001",
    "10000000000000000000000000000001",
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

    reloj = pygame.time.Clock()
    ai_settings = Settings()
    ventana = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Proyecto PRE")

    nivel = Nivel()
    muros = nivel.crearMuros(matriz_1)
    puertas = nivel.crearPuertas(matriz_1)
    siguiente_nivel = False

    #crear personaje
    personaje = Personaje(ai_settings, ventana)
    #creamos grupo proyectiles
    proyectil = pygame.sprite.Group()
    # creamos grupo enemigos
    enemigos = pygame.sprite.Group()

    fps = 60
    jugando = True
    menu_principal=True
    nivel_1 = False
    nivel_2 = False

    while jugando:
        while menu_principal:
            ventana.fill((255, 255, 205))
            opciones = [
                "new game <Press enter>",
                "Exit"
            ]
            y = 100
            for frase in opciones:
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
                        #pantalla de transición
                        texto_nivel1 = [" nivel 1 "]
                        nivel.dibujar_pantalla_transicion(ventana, texto_nivel1, fuente2, 3000)
                        personaje.reset_pos()
                        personaje.estado_inicial(enemigos)
                        enemigo1 = Enemigo(ai_settings, ventana)
                        enemigo2 = Enemigo(ai_settings, ventana)
                        enemigo3 = Enemigo(ai_settings, ventana)
                        enemigos.add(enemigo1, enemigo2, enemigo3)
                        nivel_1 = True

        while nivel_1:
            # GAME OVER
            if personaje.vida == 0:
                nivel_1 = False
                texto_GameOver = ["GAME OVER"]
                nivel.dibujar_pantalla_transicion(ventana, texto_GameOver, fuente2, 4000)
                menu_principal = True

            # actualizar ventana
            ventana.fill(ai_settings.bg_color)
            nivel.dibujar_mapa(ventana, muros, puertas, siguiente_nivel)

            #detectar controles jugador
            Personaje.check_events(ai_settings, personaje)
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
                siguiente_nivel = True
                if nivel.check_col_puerta_abierta(personaje, puertas):
                    nivel_1 = False
                    siguiente_nivel = False
                    texto_nivel2 = ["Nivel 2"]
                    nivel.dibujar_pantalla_transicion(ventana, texto_nivel2, fuente2, 3000)
                    personaje.reset_pos()
                    enemigo4 = Enemigo_tipo2(ai_settings, ventana)
                    enemigo5 = Enemigo_tipo2(ai_settings, ventana)
                    enemigos.add(enemigo4, enemigo5)
                    nivel_2 = True

        while nivel_2:
            #GAME OVER
            if personaje.vida == 0:
                nivel_2 = False
                texto_GameOver = ["GAME OVER"]
                nivel.dibujar_pantalla_transicion(ventana, texto_GameOver, fuente2, 5000)
                menu_principal = True

            # actualizar ventana
            ventana.fill(ai_settings.bg_color)
            nivel.dibujar_mapa(ventana, muros, puertas, siguiente_nivel)

            # detectar controles jugador
            Personaje.check_events(ai_settings, personaje)

            # actualizamos accion del personaje
            personaje.update(enemigos, ai_settings, ventana, personaje, proyectil, muros)

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
                texto_EndGame = ["Has ganado"]
                nivel.dibujar_pantalla_transicion(ventana, texto_EndGame, fuente2, 5000)
                menu_principal = True


if __name__ == '__main__':

    run_game()
    # Salir
    pygame.quit()
