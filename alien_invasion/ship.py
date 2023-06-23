# importing the pygame module
import pygame
from pygame.sprite import Sprite

# Building the class ship
class Ship(Sprite):
    def __init__(self, ai_settings, screen):
        """Initializing the ship and set its starting position"""
        self.screen = screen

        super().__init__()

        # Load the ship image and get its rect
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect() # getting the image rect
        self.screen_rect = screen.get_rect() # getting the screen rect

        # start each new ship at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.ai_settings = ai_settings

        # Store a decimal value for the ship's center
        self.center = float(self.rect.centerx)

        # Movement Flag
        self.moving_right = False
        self.moving_left = False

    # Center the ship
    def center_ship(self):
        """center the ship on the screen."""
        self.center = self.screen_rect.centerx

    # update the ship to respond to events
    def update(self):
        """update the ship's center value, not the rect. """
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor

        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        # update the rect object from self.center
        self.rect.centerx = self.center


    # Draw the ship to the screen
    def blitme(self):
        """Draw the ship at its current location """
        self.screen.blit(self.image, self.rect)
