import pygame

class Bird():

    def __init__(self, screen):
        """Initializes the bird and set its starting position"""
        self.screen = screen

        # Load the bird image and get rect
        self.image = pygame.image.load('images/bird_small.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # Start each bird at the bottom centerx
        self.rect.centerx = self.screen_rect.centerx
        self.rect.center = self.screen_rect.center

    def blitme(self):
        """Draw the bird at its current location"""
        self.screen.blit(self.image, self.rect)
