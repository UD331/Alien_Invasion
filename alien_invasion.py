import pygame
from pygame.sprite import Sprite
from alien import Alien
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():

    # Inititalize pygame, settings and screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Make a Ship, a group of bullets, and a group of aliens
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    # Create the fleet of aliens
    gf.create_fleet(ai_settings, screen, ships, aliens)

    # Set the background color
    bg_color = (230, 230, 230)

    # Start the main loop for the game
    while True:

        # Watch for keyboard and mouse events.
        gf.check_events(ai_settings, screen, ship, bullets)

        ship.update()

        gf.update_bullets(bullets)

        # Update images on the screen and flip to the new screen
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)

run_game()
