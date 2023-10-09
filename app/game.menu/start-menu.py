import pygame
import button

pygame.init()

# Constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 500

# Set Screen
screen = pygame.display.set_mode((SCREEN_WIDTH,  SCREEN_HEIGHT))
pygame.display.set_caption("Main Menu")

# font
font = pygame.font.SysFont("arialBlack", 40)

# Colors
TEXT_COL = (255, 255, 255)

# loading btn images
resume_img = pygame.image.load("./Fortsetzen.png").convert_alpha()

# Creating Button instances
resume_btn = button.Button((SCREEN_WIDTH/2.2), (SCREEN_HEIGHT/4), resume_img, 0.2)

# Functions
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))


run = True
game_paused = False

# Game Loop
while run:

    screen.fill((52, 78, 91))

    # Check if Game is paused
    if game_paused:
        resume_btn.draw(screen)
    else:
        draw_text("Press space for menu", font, TEXT_COL, (SCREEN_WIDTH/2.9), (SCREEN_HEIGHT/2))

    # Event Handler
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                if game_paused:
                    print("Game resumed")
                    game_paused = False
                else:
                    print("Game paused")
                    game_paused = True
            if event.key == pygame.K_q:
                print("Game exited")
                run = False
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
