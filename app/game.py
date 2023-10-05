# Example file showing a circle moving on screen
import pygame
from pygame import * 

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1600, 900))
clock = pygame.time.Clock()
dt = 0
font = pygame.font.Font("app/resources/PixelifySans-Regular.ttf", 14)

debugMode = True
running = True

#initialize some variables for the program
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)


def debugInfo():
    text = font.render(("FPS:" + str(round(clock.get_fps()))), True, (255,255,255))
    debugUI.blit(text,[10,10],None,0)


while running:
    
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")

    #add subsurface for debug UI
    debugUI = screen.subsurface(10,10,100,50)
    debugUI.fill("black")

    #init the game object and add controls
    pygame.draw.circle(screen, "red", player_pos, 40)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt

    

    # limits FPS to n
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(244) / 1000

    #debug mode - shows FPS and TPS
    if debugMode:
        debugInfo()
        
    # flip() the display to put your work on screen
    pygame.display.flip()

pygame.quit()