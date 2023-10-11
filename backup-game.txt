import pygame
from pygame import * 

debugMode = True
running = True
fullscreen = False

# TODO: make it read the settings from a file containing infos about resolution and other things, maybe even savegame stats
# pygame setup
pygame.init()

screen = pygame.display.set_mode((1920, 1080))
if fullscreen:
    screen = pygame.display.toggle_fullscreen()
pygame.display.set_caption("ArcadeFusionX")
clock = pygame.time.Clock()
dt = 0
font = pygame.font.Font("app/resources/fonts/PixelifySans-Regular.ttf", 14)



#initialize some variables for the program
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
speed = 700

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
    debugUI = screen.subsurface(10,10,75,30)
    debugUI.fill("black")

    #init the game object and add controls
    pygame.draw.circle(screen, "black", player_pos, 16)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= speed * dt
    if keys[pygame.K_s]:
        player_pos.y += speed * dt
    if keys[pygame.K_a]:
        player_pos.x -= speed * dt
    if keys[pygame.K_d]:
        player_pos.x += speed * dt
    #reset pos
    if keys[pygame.K_r]:
        player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)    

    #control movement speed
    if keys[pygame.K_f]:
        speed += 100
    if keys[pygame.K_g]:
        speed -= 100


    # limits FPS to n
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(144) / 10000

    #debug mode - shows FPS and TPS
    if debugMode:
        debugInfo()
        
    # flip() the display to put your work on screen
    pygame.display.flip()

pygame.quit()
