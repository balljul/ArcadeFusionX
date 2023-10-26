import pygame
pygame.init()


class AFX_configs():
    running = True
    SCREEN_WIDTH = 1280
    SCREEN_HEIGHT = 720
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    running = True
    dt = 0
    player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
    font = pygame.font.Font("resources/fonts/PixelifySans-Regular.ttf", 20)
    TEXT_COL = (255, 255, 255)
    keys = pygame.key.get_pressed()
