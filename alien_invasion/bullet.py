""" Importing the necessary packages """
import pygame
from settings import Settings
from pygame.sprite import Sprite

""" The class necessary for the bullet object """
class Bullet(Sprite):
    """ A class to manage bullets fired from the ship"""

    # Initializing
    def __init__(self, ai_settings, screen, ship):
        """Create a bullet object at the ship's current position. """
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Create a bullet rect at (0, 0) and then set correct position
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # Store the bullet's position as a decimal value.
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    # Update the object's location
    def update(self):
        """Move the bullet up the screen """
        # update the decimal position of the bullet
        self.y -= self.speed_factor

        # update the rect position
        self.rect.y = self.y


    # Drawing the object to the screen
    def draw_bullet(self):
        """Draw the bullet to the screen. """
        pygame.draw.rect(self.screen, self.color, self.rect)
