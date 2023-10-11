import pygame
import button
from globals import AFX_configs as configs


class Game_menu():
    # Defining constants for the menu
    screen = configs.screen
    SCREEN_WIDTH = configs.SCREEN_WIDTH
    SCREEN_HEIGHT = configs.SCREEN_HEIGHT
    font = configs.font
    TEXT_COL = configs.TEXT_COL
    game_paused = False
    # loading btn images
    resume_img = pygame.image.load("resources/resume.png").convert_alpha()
    quit_img = pygame.image.load("resources/quit.png").convert_alpha()
    options_img = pygame.image.load("resources/options.png").convert_alpha()

    # Creating Button instances
    resume_btn = button.Button((SCREEN_WIDTH/2.2), (SCREEN_HEIGHT/4), resume_img, 0.2)
    quit_btn = button.Button((SCREEN_WIDTH/2.2), (SCREEN_HEIGHT/2), quit_img, 0.2)
    options_btn = button.Button((SCREEN_WIDTH/2.2), (SCREEN_HEIGHT/1.4), options_img, 0.2)


    def draw_text(self, text, x, y):
        img = self.font.render(text, True, self.TEXT_COL)
        self.screen.blit(img, (x, y))


    def game_menu_logic(self):

        keys = configs.keys
        if keys[pygame.K_p]:
            self.game_paused = True

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
