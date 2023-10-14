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


def debugInfo():
    text = font.render(("FPS:" + str(round(clock.get_fps()))), True, (255, 255, 255))
    debugUI.blit(text, [10, 10], None, 0)


while configs.running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("blue")
    debugUI = screen.subsurface(10,10,100,50)
    debugUI.fill("black")

    keys = configs.keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 900 * dt
    if keys[pygame.K_s]:
        player_pos.y += 900 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 900 * dt
    if keys[pygame.K_d]:
        player_pos.x += 900 * dt

    if keys[pygame.K_r]:
        player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

    if keys[pygame.K_f]:
        speed += 100
    if keys[pygame.K_g]:
        speed -= 100

    if keys[pygame.K_p]:
        game_paused = True
    
    if game_paused:
        if gmenu.resume_btn.draw(screen):
            game_paused = False
        if gmenu.quit_btn.draw(screen):
            configs.running = False
        if gmenu.options_btn.draw(screen):
            pass
    else:
        pygame.draw.circle(screen, "white", player_pos, 40)
    

    dt = clock.tick(144) / 10000

    if debugMode:
        debugInfo()

    pygame.display.flip()

pygame.quit()
