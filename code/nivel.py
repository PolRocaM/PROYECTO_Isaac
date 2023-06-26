import pygame

class Nivel():

    def __init__(self):
        self.screen = pygame.display.get_surface()

        self.imagen_muro = pygame.image.load("./imagenes/Castle_Wall.png").convert()
        self.imagen_muro_redimensionado = pygame.transform.scale(self.imagen_muro, (40,40))
        self.rect = self.imagen_muro.get_rect()

        self.imagen_puerta_cerrada = pygame.image.load("./imagenes/puerta_cerrada.png").convert()
        self.imagen_puerta_cerrada_redimensionada = pygame.transform.scale(self.imagen_puerta_cerrada, (40,40))

        self.imagen_puerta_abierta = pygame.image.load("./imagenes/puerta_abierta.png").convert()
        self.imagen_puerta_abierta_redimensionada = pygame.transform.scale(self.imagen_puerta_abierta, (40, 40))

        self.imagen_lava = pygame.image.load("./imagenes/lava_1.png").convert()
        self.imagen_lava_redimensionada = pygame.transform.scale(self.imagen_lava, (40, 40))

        self.sonido_puertas = pygame.mixer.Sound('./audio/dooropened-103851.mp3')
        pygame.mixer.Sound.set_volume(self.sonido_puertas, 0.5)

    def crearMuros(self, matriz):
        muros = []
        x = 0
        y = 0
        for fila in matriz:
            for col in fila:
                if col == "1":
                    muros.append(pygame.Rect(x, y, 40, 40))
                x += 40
            x = 0
            y += 40
        return muros

    def crearPuertasSuperiores(self, matriz):
        puertas_sup = []
        x = 0
        y = 0
        for fila in matriz:
            for col in fila:
                if col == "2":
                    puertas_sup.append(pygame.Rect(x, y, 40, 40))
                x += 40
            x = 0
            y += 40
        return puertas_sup

    def crearPuertasInferiores(self, matriz):
        puertas_inf = []
        x = 0
        y = 0
        for fila in matriz:
            for col in fila:
                if col == "3":
                    puertas_inf.append(pygame.Rect(x, y, 40, 40))
                x += 40
            x = 0
            y += 40
        return puertas_inf

    def crearLava(self, matriz):
        lava = []
        x = 0
        y = 0
        for fila in matriz:
            for col in fila:
                if col == "4":
                    lava.append(pygame.Rect(x, y, 40, 40))
                x += 40
            x = 0
            y += 40
        return lava

    def dibujar_muro(self, ventana, rectangulo):
        ventana.blit(self.imagen_muro_redimensionado, rectangulo)

    def dibujar_puerta_cerrada(self, ventana, rectangulo):
        ventana.blit(self.imagen_puerta_cerrada_redimensionada, rectangulo)

    def dibujar_puerta_abierta(self, ventana, rectangulo):
        ventana.blit(self.imagen_puerta_abierta_redimensionada, rectangulo)

    def dibujar_lava(self, ventana, rectangulo):
        ventana.blit(self.imagen_lava_redimensionada, rectangulo)

    def dibujar_mapa(self, ventana, muros, puertas_sup, puertas_inf, lava, abrir_puertas):
            for muro in muros:
                self.dibujar_muro(ventana, muro)
            if abrir_puertas == True:
                for puerta in puertas_sup:
                    self.dibujar_puerta_abierta(ventana, puerta)
                for puerta in puertas_inf:
                    self.dibujar_puerta_abierta(ventana, puerta)
            elif abrir_puertas == False:
                for puerta in puertas_sup:
                    self.dibujar_puerta_cerrada(ventana, puerta)
                for puerta in puertas_inf:
                    self.dibujar_puerta_cerrada(ventana, puerta)
            for lav in lava:
                self.dibujar_lava(ventana, lav)

    def check_col_puerta_abierta(self, personaje, puertas):
        col_puerta = False
        for puerta in puertas:
            if personaje.rect.colliderect(puerta):
                col_puerta = True
                return col_puerta

    def check_col_lava(self, personaje, lava):
        for i in lava:
            if personaje.rect.colliderect(i):
                col_lava = True
                return col_lava

    def dibujar_pantalla_transicion(self, ventana, texto1, fuente, centrado_texto, delay):
        ventana.fill((0, 0, 0))
        y = 275
        for frase in texto1:
            texto = fuente.render(frase, True, (255, 255, 255))
            ventana.blit(texto, (centrado_texto, y))
            y += 40
        pygame.display.update()
        pygame.time.delay(delay)