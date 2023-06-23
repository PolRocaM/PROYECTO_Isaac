

class Settings():
    #classe per guardar totes les settings del joc
    def __init__(self):
        """Initialize the game's settings."""
        # Ventana settings.
        self.screen_width = 1280
        self.screen_height = 720
        self.bg_color = (0, 50, 0) #color negro

        # Personaje settings.
        self.personaje_speed_factor = 1

        # Proyectil settings.
        self.proyectil_speed_factor = 2
        self.proyectil_width = 15
        self.proyectil_height = 15
        self.proyectil_color = 255, 255, 255
        self.bullets_allowed = 20
        self.proyectil_dmg = 100

        # Enemigos settings
        self.enemigo_speed_factor = 0.7
        self.enemigo_dmg = 25





