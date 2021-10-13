import sys

import pygame
from bullet import Bullet

def check_events(event, ai_settings, screen, ship , bullets):
    """Respond to keypresses and mouse events."""
    for event on pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship , bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
                
def check_keydown_events(event, ai_settings, screen, ship , bullets):
        
        if event.key == pygame.K_RIGHT:
            ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            fire_bullets(ai_settings, screen, ship , bullets)
    
def check_keyup_events(event, ship):
            
                if event.key == pygame.K_RIGHT:
                    ship.moving_right = False   
                elif event.key == pygame.K_LEFT:
                    ship.moving_left = False

def fire_bullets(ai_settings, screen, ship , bullets):
    # Create a new bullet and add it to the bullets group
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def update_bullets(bullets):
    
    # Update bullets positions
    bullets.update()

    # Get rid of bullets that have disappeared
    for bullet in bullets.copy():
        if bullets.rect.bottom <= 0:
            bullets.remove(bullet)
                
def update_screen(ai_settings, screen, ship , bullets):

    # Redraw the screen during each pass through the loop
    screen.fill(ai_settings.bg_color)

    # Redraw all bullets behind ship and aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    
    ship.blitme()

    # Make the most recently drawn screen visible
    pygame.display.flip()
