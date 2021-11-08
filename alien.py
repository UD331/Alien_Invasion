import pygame
from pygame.sprite import Sprite

class Alien(Sprite):

    def _init_(self, ai_settings, screen):

        super(Alien, self)._init_()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the alien image and set its rect image
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen
        self.rect.x = self.rect.screen_width
        self.rect.y = self.rect.screen_height

        # Store the alien's exact location
        self.x = float(self.rect.x)

    def check_edges(self):

        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= screen_rect.left:
            return True

    def update(self):

        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x;

    def blitme(self):

        self.screen.blit(self.image, self.rect)
