import pygame
from menus import AFX_menus
from globals import AFX_configs

pygame.init()
menus = AFX_menus()
configs = AFX_configs()
pygame.display.set_caption("AcradeFusionX")

fullscreen = False
debugMode = True
screen = configs.screen
clock = configs.clock
dt = configs.dt
player_pos = configs.player_pos
font = configs.font
speed = 700
game_state = "start_menu"

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
    debugUI = screen.subsurface(10, 10, 100, 50)
    debugUI.fill("black")

    keys = pygame.key.get_pressed()

    if keys[pygame.K_q]:
        configs.running = False
    

    if game_state == "start_menu":
        if menus.start_btn.draw(screen):
            game_state = "game"
    elif game_state == "game":

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
            game_state = "game_menu"

        pygame.draw.circle(screen, "white", player_pos, 40)

    elif game_state == "game_menu":
        if menus.resume_btn.draw(screen):
            game_state = "game"
        if menus.quit_btn.draw(screen):
            game_state = "start_menu"

    dt = clock.tick(144) / 10000

    if debugMode:
        debugInfo()

    pygame.display.flip()

pygame.quit()
