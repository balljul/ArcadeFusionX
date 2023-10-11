# Example file showing a circle moving on screen
import pygame
from menus import Game_menu as gmenu
from globals import AFX_configs as configs
# pygame setup
pygame.init()

screen = configs.screen
clock = configs.clock
running = configs.running
dt = configs.dt

player_pos = configs.player_pos

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("blue")

    pygame.draw.circle(screen, "white", player_pos, 40)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 900 * dt
    if keys[pygame.K_s]:
        player_pos.y += 900 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 900 * dt
    if keys[pygame.K_d]:
        player_pos.x += 900 * dt

    pygame.display.flip()

pygame.quit()
