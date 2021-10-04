import pygame

class Ship():

    def _init_(self, screen):
        """Inititalize the ship and set its starting position."""
        self.screen = screen

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each ship at the bottom of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        def blitme(self):
            """Fraw the ship at its current location."""
            self.screen.blit(self.image, self.rect)
            
