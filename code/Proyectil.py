import pygame
from pygame.sprite import Sprite

class Proyectil(Sprite):
    def __init__(self, ai_settings, ventana, personaje, direccion):
        super(Proyectil, self).__init__()
        self.ventana = ventana
        self.image = pygame.image.load("./imagenes/bubble.png")

        # Create bullet rect at (0, 0), then set correct position.
        self.rect = self.image.get_rect()
        # self.rect = pygame.Rect(0, 0, ai_settings.proyectil_width, ai_settings.proyectil_height)
        self.rect.centerx = personaje.rect.centerx
        self.rect.centery = personaje.rect.centery

        # Store a decimal value for the bullet's position.
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)

        self.color = ai_settings.proyectil_color
        self.speed_factor = ai_settings.proyectil_speed_factor
        self.direccion = direccion



    def update(self):

        #Mover el proyectil
        if self.direccion == pygame.K_UP:
            # self.image = pygame.image.load("./imagenes/bullet_u.png")
            # Update the decimal position of the bullet (UP).
            self.y -= self.speed_factor
            # Update the rect position.
            self.rect.y = self.y
        elif self.direccion == pygame.K_DOWN:
            # self.image = pygame.image.load("./imagenes/bullet_d.png")
            # Update the decimal position of the bullet (DOWN).
            self.y += self.speed_factor
            # Update the rect position.
            self.rect.y = self.y
        elif self.direccion == pygame.K_RIGHT:
            # self.image = pygame.image.load("./imagenes/bullet_r.png")
            # Update the decimal position of the bullet (RIGHT).
            self.x += self.speed_factor
            # Update the rect position.
            self.rect.x = self.x

        elif self.direccion == pygame.K_LEFT:
            # self.image = pygame.image.load("./imagenes/bullet_l.png")
            # Update the decimal position of the bullet (LEFT).
            self.x -= self.speed_factor
            # Update the rect position.
            self.rect.x = self.x

    def draw_bullet(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.ventana, self.color, self.rect)


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
