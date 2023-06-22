import pygame
from enum import Enum
import math

class MapPart(Enum):
    WALL = (1, "Castle_wall.png", True)
    FLOOR = (0, "suelo.png", False)

    def __new__(cls, value, texture, collision):
        obj = object.__new__(cls)
        obj._value_ = value
        obj.texture = pygame.image.load("suelo.png")
        # obj.texture = pygame.transform.scale(pygame.image.load("suelo.png").convert(),(80, 80))
        obj.collision = collision
        return obj


class Mapa:
    def __init__(self, matriz):
        self.matriz = matriz
        self.sprites = pygame.sprite.Group()
        self.collision_sprites = pygame.sprite.Group()

        for y, fila in enumerate(matriz):
            for x, valor in enumerate(fila):
                if valor == MapPart.WALL.value:  
                    sprite = pygame.sprite.Sprite()
                    sprite.image = MapPart.WALL.texture
                    sprite.rect = sprite.image.get_rect()
                    sprite.rect.x = x * 80
                    sprite.rect.y = y * 80
                    self.sprites.add(sprite)
                    if MapPart.WALL.collision:
                        self.collision_sprites.add(sprite)
                    
                elif valor == MapPart.FLOOR.value:  
                    sprite = pygame.sprite.Sprite()
                    sprite.image = MapPart.FLOOR.texture
                    sprite.rect = sprite.image.get_rect()
                    sprite.rect.x = x * 80
                    sprite.rect.y = y * 80
                    self.sprites.add(sprite)
                
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 720))

    ####################################
    def draw_player(self, x, y):
        player_rect = pygame.Rect(x, y, 50, 50)
        pygame.draw.rect(self.screen, (0, 255, 0), player_rect)


    def run(self):
        player_rect = pygame.Rect(0, 0, 50, 50)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

            self.draw(player_rect)
    
    def check_collision(self, x, y):
        player_rect = pygame.Rect(x, y, 100, 100)
        for sprite in self.collision_sprites:
            if player_rect.colliderect(sprite.rect):
                return True
        return False
