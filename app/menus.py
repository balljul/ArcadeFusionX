import pygame
import button
from globals import AFX_configs as configs


class Game_menu():
    def __init__(self, font=configs.font, text_col=configs.TEXT_COL, screenw=configs.SCREEN_WIDTH, screenh=configs.SCREEN_HEIGHT):
        # Defining constants for the menu
        self.screen = pygame.display.set_mode((screenw,  screenh))
        self.SCREEN_WIDTH = screenw
        self.SCREEN_HEIGHT = screenh
        self.font = font
        self.TEXT_COL = text_col
        self.game_paused = False

        # loading btn images
        self.resume_img = pygame.image.load("./resume.png").convert_alpha()
        self.quit_img = pygame.image.load("./quit.png").convert_alpha()
        self.options_img = pygame.image.load("./options.png").convert_alpha()

        # Creating Button instances
        self.resume_btn = button.Button((SCREEN_WIDTH/2.2), (SCREEN_HEIGHT/4), resume_img, 0.2)
        self.quit_btn = button.Button((SCREEN_WIDTH/2.2), (SCREEN_HEIGHT/2), quit_img, 0.2)
        self.options_btn = button.Button((SCREEN_WIDTH/2.2), (SCREEN_HEIGHT/1.4), options_img, 0.2)


def draw_text(self, text, x, y):
    img = self.font.render(text, True, self.TEXT_COL)
    self.screen.blit(img, (x, y))


def game_menu_Logic(self):

    # Check if Game is paused
    if self.game_paused:
        if self.resume_btn.draw(self.screen):
            self.game_paused = False
        if self.quit_btn.draw(self.screen):
            configs.running = False
        if self.options_btn.draw(self.screen):
            pass
        else:
            self.draw_text("Press space for menu", self.font, self.TEXT_COL, (self.SCREENW/2.9), (self.SCREEN_HEIGHT/2))
