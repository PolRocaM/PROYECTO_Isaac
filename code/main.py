import random
import sys
import pygame
from nivel import Nivel
from Personaje import Personaje
from settings import Settings
from Proyectil import Proyectil
from enemigo import Enemigo
from enemigo_tipo1 import Enemigo_tipo1
from enemigo_tipo2 import Enemigo_tipo2
from enemigoBoss import Enemigo_Boss
import niveles

pygame.init()

fuente1 = pygame.font.SysFont("arial black", 24)
fuente2 = pygame.font.SysFont("Segoe print", 32)
texto_nivel1 = [" Entering the dungeon... "]
texto_GameOver = ["GAME OVER"]
reloj = pygame.time.Clock()
ai_settings = Settings()
ventana = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
pygame.display.set_caption("Proyecto PRE")
nivel = Nivel()

def run_game():
    nivel_actual = 0
    nivel_1 = nivel_2 = nivel_3 = nivel_4 = nivel_5 = False
    abrir_puertas = False
    enemigos_eliminados_nivel2 = False
    enemigos_eliminados_nivel3 = False
    enemigos_eliminados_nivel4 = False
    enemigos_eliminados_nivel5 = False
    sonido_puerta_1 = False
    sonido_puerta_2 = False
    sonido_puerta_3 = False
    sonido_puerta_4 = False
    sonido_puerta_5 = False

    #crear personaje
    personaje = Personaje(ai_settings, ventana)
    #creamos grupo proyectiles
    proyectil = pygame.sprite.Group()
    # creamos grupo enemigos
    enemigos = pygame.sprite.Group()

    rand1 = random.randrange(1) + 1
    rand2 = random.randrange(2) + 1
    rand3 = random.randrange(3) + 1

    fps = 60
    jugando = True
    menu_principal=True

    while jugando:
        if nivel_actual == 0:
            menu_principal = True
            pygame.mixer.music.load('./audio/Cube World Intro Menu Music.mp3')
            pygame.mixer.music.play(-1)
            pygame.mixer.music.set_volume(0.2)
        elif nivel_actual == 1:
            pygame.mixer.music.load('./audio/Hollow Knight OST.mp3')
            pygame.mixer.music.play(-1)
            pygame.mixer.music.set_volume(0.1)
            nivel_1 = True
        elif nivel_actual == 2:
            nivel_2 = True
        elif nivel_actual == 3:
            nivel_3 = True
        elif nivel_actual == 4:
            nivel_4 = True
        elif nivel_actual == 5:
            nivel_5 = True

        muros = muros_nivel(nivel, nivel_actual)
        puertas_sup = puertas_sup_nivel(nivel, nivel_actual)
        puertas_inf = puertas_inf_nivel(nivel, nivel_actual)
        lava = lava_nivel(nivel, nivel_actual)

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
                        pygame.mixer.music.stop()
                        #pantalla de transición
                        nivel.dibujar_pantalla_transicion(ventana, texto_nivel1, fuente2, 400, 3000)
                        abrir_puertas = False
                        enemigos_eliminados_nivel2 = False
                        enemigos_eliminados_nivel3 = False
                        enemigos_eliminados_nivel4 = False
                        sonido_puerta_1 = False
                        sonido_puerta_2 = False
                        sonido_puerta_3 = False
                        sonido_puerta_4 = False
                        sonido_puerta_5 = False
                        personaje.reset_inicial(enemigos)
                        personaje.estado_inicial()
                        for x in range(rand1):
                            enemigo = Enemigo_tipo1(ai_settings, ventana)
                            enemigos.add(enemigo)
                        nivel_actual = 1
        while nivel_1:
            # GAME OVER
            if personaje.vida == 0:
                nivel_actual = 0
                nivel_1 = False
                nivel.dibujar_pantalla_transicion(ventana, texto_GameOver, fuente2, 525, 5000)
                menu_principal = True

            # actualizar ventana
            ventana.fill(ai_settings.bg_color)
            nivel.dibujar_mapa(ventana, muros, puertas_sup, puertas_inf, lava, abrir_puertas)

            #detectar controles jugador
            Personaje.check_events(ai_settings, personaje)
            personaje.recibir_danyo_lava(ai_settings, nivel, lava)
            personaje.update(enemigos, ai_settings, ventana, personaje, proyectil, muros)

            #actualizamos proyectiles
            Proyectil.update_bullets(proyectil, ai_settings, muros)

            # dibujar personaje
            personaje.blitme()
            personaje.draw_barra_vida(personaje.vida)

            #actualizamos enemigos
            #Enemigo.update_enemigos(enemigos, personaje, ai_settings)
            for enemigo in enemigos:
                enemigo.update(personaje, enemigos, ai_settings)
                enemigo.update_vida(ai_settings, proyectil, enemigos, personaje)
                enemigo.update_barra_vida(enemigo)
            enemigos.draw(ventana)

            proyectil.draw(ventana)

            # reloj.tick(fps)
            pygame.display.update()
            pygame.display.flip() # Make the most recently drawn screen visible.

            #transicio a nivel 2
            if len(enemigos) == 0:
                if sonido_puerta_1 == False:
                    nivel.sonido_puertas.play()
                    sonido_puerta_1 = True
                abrir_puertas = True
                #subir de sala
                if nivel.check_col_puerta_abierta(personaje, puertas_sup):
                    nivel_1 = False
                    abrir_puertas = False
                    personaje.reset_pos_sup()
                    if enemigos_eliminados_nivel2 == False:
                        for x in range(rand2):
                            enemigo = Enemigo_tipo2(ai_settings, ventana)
                            enemigos.add(enemigo)
                    nivel_actual += 1

        while nivel_2:
            #GAME OVER
            if personaje.vida == 0:
                nivel_actual = 0
                nivel_2 = False
                nivel.dibujar_pantalla_transicion(ventana, texto_GameOver, fuente2, 530, 5000)
                menu_principal = True

            # actualizar ventana
            ventana.fill(ai_settings.bg_color)
            nivel.dibujar_mapa(ventana, muros, puertas_sup, puertas_inf, lava, abrir_puertas)

            Personaje.check_events(ai_settings, personaje)
            personaje.recibir_danyo_lava(ai_settings, nivel, lava)
            personaje.update(enemigos, ai_settings, ventana, personaje, proyectil, muros)

            # actualizamos proyectiles
            Proyectil.update_bullets(proyectil, ai_settings, muros)

            for enemigo in enemigos:
                enemigo.update(personaje, enemigos, ai_settings)
                enemigo.update_vida(ai_settings, proyectil, enemigos, personaje)
                enemigo.update_barra_vida(enemigo)
            enemigos.draw(ventana)

            # dibujar personaje
            personaje.blitme()
            personaje.draw_barra_vida(personaje.vida)

            proyectil.draw(ventana)
            pygame.display.update()
            # reloj.tick(fps)
            # Make the most recently drawn screen visible.
            pygame.display.flip()

            # transicio a nivel 3
            if len(enemigos) == 0:
                if sonido_puerta_2 == False:
                    nivel.sonido_puertas.play()
                    sonido_puerta_2 = True
                enemigos_eliminados_nivel2 = True
                abrir_puertas = True
                # subir de sala
                if nivel.check_col_puerta_abierta(personaje, puertas_sup):
                    nivel_2 = False
                    abrir_puertas = False
                    personaje.reset_pos_sup()
                    if enemigos_eliminados_nivel3 == False:
                        for x in range(rand1):
                            enemigo = Enemigo_tipo1(ai_settings, ventana)
                            enemigos.add(enemigo)
                        for y in range(rand3):
                            enemigo = Enemigo_tipo2(ai_settings, ventana)
                            enemigos.add(enemigo)
                    nivel_actual += 1
                # bajar de sala
                if nivel.check_col_puerta_abierta(personaje, puertas_inf):
                    nivel_2 = False
                    abrir_puertas = False
                    personaje.reset_pos_inf()
                    nivel_actual -= 1

        while nivel_3:
            # GAME OVER
            if personaje.vida == 0:
                nivel_actual = 0
                nivel_3 = False
                nivel.dibujar_pantalla_transicion(ventana, texto_GameOver, fuente2, 530, 5000)
                menu_principal = True

            # actualizar ventana
            ventana.fill(ai_settings.bg_color)
            nivel.dibujar_mapa(ventana, muros, puertas_sup, puertas_inf, lava, abrir_puertas)

            # detectar controles jugador
            Personaje.check_events(ai_settings, personaje)
            personaje.recibir_danyo_lava(ai_settings, nivel, lava)
            personaje.update(enemigos, ai_settings, ventana, personaje, proyectil, muros)

            # actualizamos proyectiles
            Proyectil.update_bullets(proyectil, ai_settings, muros)

            for enemigo in enemigos:
                enemigo.update(personaje, enemigos, ai_settings)
                enemigo.update_vida(ai_settings, proyectil, enemigos, personaje)
                enemigo.update_barra_vida(enemigo)
            enemigos.draw(ventana)

            # dibujar personaje
            personaje.blitme()
            personaje.draw_barra_vida(personaje.vida)

            proyectil.draw(ventana)
            pygame.display.update()
            # reloj.tick(fps)
            # Make the most recently drawn screen visible.
            pygame.display.flip()

            #transicio a nivel boss
            if len(enemigos) == 0:
                if sonido_puerta_3 == False:
                    nivel.sonido_puertas.play()
                    sonido_puerta_3 = True
                enemigos_eliminados_nivel3 = True
                abrir_puertas = True
                if nivel.check_col_puerta_abierta(personaje, puertas_sup):
                    nivel_3 = False
                    abrir_puertas = False
                    personaje.reset_pos_sup()
                    if enemigos_eliminados_nivel4 == False:
                        for x in range(rand3):
                            enemigo = Enemigo_tipo1(ai_settings, ventana)
                            enemigos.add(enemigo)
                        for y in range(rand3):
                            enemigo = Enemigo_tipo2(ai_settings, ventana)
                            enemigos.add(enemigo)
                    nivel_actual += 1
                # bajar de sala
                if nivel.check_col_puerta_abierta(personaje, puertas_inf):
                    nivel_3 = False
                    abrir_puertas = False
                    personaje.reset_pos_inf()
                    nivel_actual -= 1

        while nivel_4:
            # GAME OVER
            if personaje.vida == 0:
                nivel_actual = 0
                nivel_4 = False
                nivel.dibujar_pantalla_transicion(ventana, texto_GameOver, fuente2, 530, 5000)
                menu_principal = True

            # actualizar ventana
            ventana.fill(ai_settings.bg_color)
            nivel.dibujar_mapa(ventana, muros, puertas_sup, puertas_inf, lava, abrir_puertas)

            # detectar controles jugador
            Personaje.check_events(ai_settings, personaje)
            personaje.recibir_danyo_lava(ai_settings, nivel, lava)
            personaje.update(enemigos, ai_settings, ventana, personaje, proyectil, muros)

            # actualizamos proyectiles
            Proyectil.update_bullets(proyectil, ai_settings, muros)

            for enemigo in enemigos:
                enemigo.update(personaje, enemigos, ai_settings)
                enemigo.update_vida(ai_settings, proyectil, enemigos, personaje)
                enemigo.update_barra_vida(enemigo)
            enemigos.draw(ventana)

            # dibujar personaje
            personaje.blitme()
            personaje.draw_barra_vida(personaje.vida)

            proyectil.draw(ventana)
            pygame.display.update()
            # reloj.tick(fps)
            # Make the most recently drawn screen visible.
            pygame.display.flip()

            # transicio a nivel boss
            if len(enemigos) == 0:
                if sonido_puerta_4 == False:
                    nivel.sonido_puertas.play()
                    sonido_puerta_4 = True
                enemigos_eliminados_nivel4 = True
                abrir_puertas = True
                if nivel.check_col_puerta_abierta(personaje, puertas_sup):
                    nivel_4 = False
                    abrir_puertas = False
                    personaje.reset_pos_sup()
                    if enemigos_eliminados_nivel5 == False:
                        enemigo = Enemigo_Boss(ai_settings, ventana)
                        enemigos.add(enemigo)
                        pygame.mixer.music.load('./audio/Godskin Apostles.mp3')
                        pygame.mixer.music.play(-1)
                        pygame.mixer.music.set_volume(0.1)
                    nivel_actual += 1
                # bajar de sala
                if nivel.check_col_puerta_abierta(personaje, puertas_inf):
                    nivel_4 = False
                    abrir_puertas = False
                    personaje.reset_pos_inf()
                    nivel_actual -= 1


        while nivel_5:
            # GAME OVER
            if personaje.vida == 0:
                nivel_actual = 0
                nivel_5 = False
                nivel.dibujar_pantalla_transicion(ventana, texto_GameOver, fuente2, 530, 5000)
                menu_principal = True

            # actualizar ventana
            ventana.fill(ai_settings.bg_color)
            nivel.dibujar_mapa(ventana, muros, puertas_sup, puertas_inf, lava, abrir_puertas)

            # detectar controles jugador
            Personaje.check_events(ai_settings, personaje)
            personaje.recibir_danyo_lava(ai_settings, nivel, lava)
            personaje.update(enemigos, ai_settings, ventana, personaje, proyectil, muros)

            # actualizamos proyectiles
            Proyectil.update_bullets(proyectil, ai_settings, muros)

            # dibujar personaje
            personaje.blitme()
            personaje.draw_barra_vida(personaje.vida)

            for enemigo in enemigos:
                enemigo.update(personaje, enemigos, ai_settings)
                enemigo.update_vida(ai_settings, proyectil, enemigos, personaje)
                enemigo.update_barra_vida(enemigo)
            enemigos.draw(ventana)

            proyectil.draw(ventana)
            pygame.display.update()
            # reloj.tick(fps)
            # Make the most recently drawn screen visible.
            pygame.display.flip()

            if len(enemigos) == 0:
                if sonido_puerta_5 == False:
                    nivel.sonido_puertas.play()
                    sonido_puerta_5 = True
                enemigos_eliminados_nivel5 = True
                abrir_puertas = True
                if nivel.check_col_puerta_abierta(personaje, puertas_sup):
                    nivel_5 = False
                    texto_EndGame = ["Dungeon cleared successfully"]
                    nivel.dibujar_pantalla_transicion(ventana, texto_EndGame, fuente2, 400, 5000)
                    nivel_actual = 0
                    menu_principal = True
                if nivel.check_col_puerta_abierta(personaje, puertas_inf):
                    nivel_5 = False
                    abrir_puertas = False
                    personaje.reset_pos_inf()
                    pygame.mixer.music.load('./audio/Hollow Knight OST.mp3')
                    pygame.mixer.music.play(-1)
                    pygame.mixer.music.set_volume(0.1)
                    nivel_actual -= 1


def muros_nivel(nivel, nivel_actual):
    if nivel_actual == 0 or nivel_actual == 1:
        muros = nivel.crearMuros(niveles.matriz_1)
        return muros
    if nivel_actual == 2:
        muros = nivel.crearMuros(niveles.matriz_2)
        return muros
    if nivel_actual == 3:
        muros = nivel.crearMuros(niveles.matriz_3)
        return muros
    if nivel_actual == 4:
        muros = nivel.crearMuros(niveles.matriz_4)
        return muros
    if nivel_actual == 5:
        muros = nivel.crearMuros(niveles.matriz_5)
        return muros

def puertas_sup_nivel(nivel, nivel_actual):
    if nivel_actual == 0 or nivel_actual == 1:
        puertas_sup = nivel.crearPuertasSuperiores(niveles.matriz_1)
        return puertas_sup
    if nivel_actual == 2:
        puertas_sup = nivel.crearPuertasSuperiores(niveles.matriz_2)
        return puertas_sup
    if nivel_actual == 3:
        puertas_sup = nivel.crearPuertasSuperiores(niveles.matriz_3)
        return puertas_sup
    if nivel_actual == 4:
        puertas_sup = nivel.crearPuertasSuperiores(niveles.matriz_4)
        return puertas_sup
    if nivel_actual == 5:
        puertas_sup = nivel.crearPuertasSuperiores(niveles.matriz_5)
        return puertas_sup

def puertas_inf_nivel(nivel, nivel_actual):
    if nivel_actual == 0 or nivel_actual == 1:
        puertas_inf = nivel.crearPuertasInferiores(niveles.matriz_1)
        return puertas_inf
    if nivel_actual == 2:
        puertas_inf = nivel.crearPuertasInferiores(niveles.matriz_2)
        return puertas_inf
    if nivel_actual == 3:
        puertas_inf = nivel.crearPuertasInferiores(niveles.matriz_3)
        return puertas_inf
    if nivel_actual == 4:
        puertas_inf = nivel.crearPuertasInferiores(niveles.matriz_4)
        return puertas_inf
    if nivel_actual == 5:
        puertas_inf = nivel.crearPuertasInferiores(niveles.matriz_5)
        return puertas_inf

def lava_nivel(nivel, nivel_actual):
    if nivel_actual == 0 or nivel_actual == 1:
        lava = nivel.crearLava(niveles.matriz_1)
        return lava
    if nivel_actual == 2:
        lava = nivel.crearLava(niveles.matriz_2)
        return lava
    if nivel_actual == 3:
        lava = nivel.crearLava(niveles.matriz_3)
        return lava
    if nivel_actual == 4:
        lava = nivel.crearLava(niveles.matriz_4)
        return lava
    if nivel_actual == 5:
        lava = nivel.crearLava(niveles.matriz_5)
        return lava

if __name__ == '__main__':
    run_game()
    pygame.quit()
