import pygame
from pygame.sprite import Sprite
from settings import Settings
from game_stats import GameStats
from ship import Ship
from button import Button
import game_functions as gf

def run_game():

    # Inititalize pygame, settings and screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Make the Play Button
    play_button = Button(ai_settings, screen, "Play")

    # Create an instance to store game statistics
    stats = GameStats(ai_settings)

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

        gf.check_events(ai_settings, screen, stats, play_button, ship, aliens, bullets)

        if stats.game_active:
            ship.update()

            gf.update_bullets(ai_settings, stats, screen, ship, aliens, bullets)

            gf.update_aliens(ai_settings, ship, aliens)

        gf.update_screen(ai_settings, screen, stats, ship, aliens, bullets, play_button)

run_game()
