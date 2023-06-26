import pygame
from pygame.sprite import Sprite

class Proyectil(Sprite):
    def __init__(self, ai_settings, ventana, personaje, direccion):
        super(Proyectil, self).__init__()
        self.ventana = ventana
        self.image = pygame.image.load("./imagenes/bubble.png")

        self.rect = self.image.get_rect()
        self.rect.centerx = personaje.rect.centerx
        self.rect.centery = personaje.rect.centery

        self.y = float(self.rect.y)
        self.x = float(self.rect.x)

        self.speed_factor = ai_settings.proyectil_speed_factor
        self.direccion = direccion


    def update(self):

        #Mover el proyectil
        if self.direccion == pygame.K_UP:
            # self.image = pygame.image.load("./imagenes/bullet_u.png")
            self.y -= self.speed_factor
            self.rect.y = self.y
        elif self.direccion == pygame.K_DOWN:
            # self.image = pygame.image.load("./imagenes/bullet_d.png")
            self.y += self.speed_factor
            self.rect.y = self.y
        elif self.direccion == pygame.K_RIGHT:
            # self.image = pygame.image.load("./imagenes/bullet_r.png")
            self.x += self.speed_factor
            self.rect.x = self.x

        elif self.direccion == pygame.K_LEFT:
            # self.image = pygame.image.load("./imagenes/bullet_l.png")
            self.x -= self.speed_factor
            self.rect.x = self.x

    def fire_bullet(ai_settings, ventana, personaje, proyectil, direccion):
        """Fire a bullet, if limit not reached yet."""
        # Create a new bullet, add to bullets group.
        if len(proyectil) < ai_settings.bullets_allowed: #limitar les bales
            new_bullet = Proyectil(ai_settings, ventana, personaje, direccion)
            proyectil.add(new_bullet)

    def update_bullets(proyectil, ai_settings, muros):
        """Update position of bullets, and get rid of old bullets."""
        # Update bullet positions.
        proyectil.update()

        for bullet in proyectil:
            # # Borrar balas que se van de la pantalla
            if bullet.rect.bottom <= 0 or bullet.rect.top >= ai_settings.screen_height or bullet.rect.right <= 0 or bullet.rect.left >= ai_settings.screen_width:
                proyectil.remove(bullet)
            # borrar balas que colisionan con los muros
            for muro in muros:
                if bullet.rect.colliderect(muro):
                    proyectil.remove(bullet)
