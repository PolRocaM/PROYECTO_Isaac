import os
import pygame

images = {
        "muro": pygame.transform.scale(pygame.image.load("Castle_Wall.png"), (80, 80)),
        "hierba": pygame.transform.scale(pygame.image.load("suelo.png"), (80, 80)),
    }


class Mapa():
    layout = [
    "XXXXXXXXXXXXXXXX",
    "X              X",
    "X              X",
    "X         X    X",
    "X              X",
    "X  X           X",
    "X              X",
    "X              X",
    "XXXXXXXXXXXXXXXX"
    ]



    images = []

    def dibujarRectangulo(self, ventana, rectangulo,tipo):
        ventana.blit(images[tipo],rectangulo)
    
    def construir_mapa(self, ventana):
        muros = []
        x = 0
        y = 0
        for muro in self.layout:
            for ladrillo in muro:
                if ladrillo == "e":
                    a = pygame.Rect(x, y, 80, 80)
                    self.dibujarRectangulo(ventana, a, 'muro')
                    muros.append((a, 'muro'))
                elif ladrillo == "G":
                    a = pygame.Rect(x, y, 80, 80)
                    self.dibujarRectangulo(ventana, a, 'hierba')
                    muros.append((a,'hierba'))
                x += 80
            x = 0
            y += 80
        return muros
    