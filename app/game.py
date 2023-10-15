import pygame
from menus import Game_menu
from globals import AFX_configs as configs

pygame.init()
gmenu = Game_menu()
pygame.display.set_caption("AcradeFusionX")

fullscreen = False
debugMode = True
screen = configs.screen
clock = configs.clock
dt = configs.dt
player_pos = configs.player_pos
font = configs.font
speed = 700
game_paused = False

if fullscreen:
    screen = pygame.display.toggle_fullscreen()

debugUI = screen.subsurface(10, 10, 100, 40)

def debugInfo():
    #debug UI elements
    debugUI.fill("black")
    text = font.render(("FPS:" + str(round(clock.get_fps()))), True, (255, 255, 255))
    debugUI.blit(text, [10, 10], None, 0)

while configs.running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            configs.running = False

    screen.fill('#242424')

    #controls
    keys = configs.keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= speed * dt
    if keys[pygame.K_s]:
        player_pos.y += speed * dt
    if keys[pygame.K_a]:
        player_pos.x -= speed * dt
    if keys[pygame.K_d]:
        player_pos.x += speed * dt

    if keys[pygame.K_r]:
        player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

    if keys[pygame.K_f]:
        speed += 100
    if keys[pygame.K_g]:
        speed -= 100

    if keys[pygame.K_p]:
        game_paused = True
        pygame.time.wait(100)

    if game_paused:
        if gmenu.resume_btn.draw(screen):
            game_paused = False
        if gmenu.quit_btn.draw(screen):
            configs.running = False
        if gmenu.options_btn.draw(screen):
            pass

    else:
        pygame.draw.circle(screen, '#AF0000', player_pos, 30)

    dt = clock.tick(240) / 10000

    if debugMode:
        debugInfo()

    pygame.display.flip()

pygame.quit()
