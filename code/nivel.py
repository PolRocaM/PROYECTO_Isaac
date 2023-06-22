import pygame
from Tiles import Tile


class Nivel():

    def __init__(self):
        self.screen = pygame.display.get_surface()
        self.image = pygame.image.load("suelo.png").convert()
        self.rect = self.image.get_rect()

    def crearMapa(self, matriz):
        muros = []
        x = 0
        y = 0
        for fila in matriz:
            for muro in fila:
                if muro == "1":
                    muros.append(pygame.Rect(x, y, 80, 80))
                x += 80
            x = 0
            y += 80
        return muros


    def dibujar_muro(self, ventana, rectangulo):
        ventana.blit(self.image, rectangulo)

    def dibujar_mapa(self, ventana, muros):
        for muro in muros:
            self.dibujar_muro(ventana, muro)
