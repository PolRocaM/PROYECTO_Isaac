
class Settings():
    #classe per guardar totes les settings del joc
    def __init__(self):
        """Initialize the game's settings."""
        # Ventana settings.
        self.screen_width = 1280
        self.screen_height = 720
        self.bg_color = (137, 107, 73) #color marron

        # Personaje settings.
        self.personaje_speed_factor = 1

        # Proyectil settings.
        self.proyectil_speed_factor = 1
        self.proyectil_width = 15
        self.proyectil_height = 15
        self.proyectil_color = 255, 255, 255
        self.bullets_allowed = 20
        self.proyectil_dmg = 200

        # Enemigos settings
        self.enemigo_speed_factor = 0.7
        self.boss_speed_factor = 0.2
        self.dmg_enemigo = 10

        self.dmg_lava = 10




