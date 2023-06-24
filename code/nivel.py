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

    def crearPuertas(self, matriz):
        puertas = []
        x = 0
        y = 0
        for fila in matriz:
            for col in fila:
                if col == "2":
                    puertas.append(pygame.Rect(x, y, 40, 40))
                x += 40
            x = 0
            y += 40
        return puertas

    def dibujar_muro(self, ventana, rectangulo):
        ventana.blit(self.imagen_muro_redimensionado, rectangulo)

    def dibujar_puerta_cerrada(self, ventana, rectangulo):
        ventana.blit(self.imagen_puerta_cerrada_redimensionada, rectangulo)

    def dibujar_puerta_abierta(self, ventana, rectangulo):
        ventana.blit(self.imagen_puerta_abierta_redimensionada, rectangulo)

    def dibujar_mapa(self, ventana, muros, puertas, sig_nivel):
            for muro in muros:
                self.dibujar_muro(ventana, muro)
            if sig_nivel == True:
                for puerta in puertas:
                    self.dibujar_puerta_abierta(ventana, puerta)
            if sig_nivel == False:
                for puerta in puertas:
                    self.dibujar_puerta_cerrada(ventana, puerta)

    def check_col_puerta_abierta(self, personaje, puertas):
        col_puerta = False
        for puerta in puertas:
            if personaje.rect.colliderect(puerta):
                col_puerta = True
                return col_puerta

    def dibujar_pantalla_transicion(self, ventana, texto1, fuente, delay):
        ventana.fill((0, 0, 0))
        y = 275
        for frase in texto1:
            texto = fuente.render(frase, True, (255, 255, 255))
            ventana.blit(texto, (540, y))
            y += 40
        pygame.display.update()
        pygame.time.delay(delay)