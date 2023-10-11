import pygame
pygame.init()


class AFX_configs():
    def __init__(self):
        self.run = True
        self.SCREEN_WIDTH = 1920
        self.SCREEN_HEIGHT = 1080
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        self.dt = 0
        self.player_pos = pygame.Vector2(self.screen.get_width() / 2, self.screen.get_height() / 2)
        self.font = pygame.font.SysFont("arialBlack", 40)
        self.TEXT_COL = (255, 255, 255)
        self.keys = pygame.key.get_pressed()
