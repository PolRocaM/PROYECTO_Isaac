import pygame

class Nivel():

    def __init__(self):
        self.screen = pygame.display.get_surface()
        self.image = pygame.image.load("suelo.png").convert()
        self.image_redimensionada = pygame.transform.scale(self.image, (40,40))
        self.rect = self.image.get_rect()

        self.next_level = False

    def crearMapa(self, matriz):
        muros = []
        puerta = []
        x = 0
        y = 0
        for fila in matriz:
            for muro in fila:
                if muro == "1":
                    muros.append(pygame.Rect(x, y, 40, 40))
                if muro == "2":
                    puerta.append(pygame.Rect(x, y, 40, 40))
                x += 40
            x = 0
            y += 40
        return muros


    def dibujar_muro(self, ventana, rectangulo):
        ventana.blit(self.image_redimensionada, rectangulo)

    def dibujar_mapa(self, ventana, muros):
        for muro in muros:
            self.dibujar_muro(ventana, muro)

    def check_siguiente_nivel(self, enemigos):
        pass

        # if self.next_level == True:
        #     print("siguiente nivel")
        #     self.next_level = False