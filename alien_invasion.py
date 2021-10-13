import pygame
from pygame.sprite import Sprite

from settings import Settings
from ship import Ship
from game_functions import as gf

def run_game():
    # Inititalize pygame, settings and screen object.
    pygame.intit()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Make a Ship
    ship = Ship(ai_settings, screen)
    # Make a group to store bullets in
    bullets = Group()
    
    # Set the background color
    bg_color = (230, 230, 230)

    # Start the main loop for the game
    while True:

        # Watch for keyboard and mouse events.
        gf.check_events(ai_settings, screen, ship, bullets)

        ship.update()

        gf.update_bullets(bullets)
        
        # Update images on the screen and flip to the new screen
        gf.update_screen(ai_settings, screen, ship, bullets)

run_game()
