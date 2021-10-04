import sys

import pygame

def check_events():
    """Respond to keypresses and mouse events"""
    for event on pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def update_screen():
    """Update images on the screen and flip to the new screen
    # Redraw the screen during each pass through the loop
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    # Make the most recently drawn screen visible
    pygame.display.flip()
