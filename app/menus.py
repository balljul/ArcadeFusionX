import pygame
import button
from globals import AFX_configs as configs


class AFX_menus():
    # Defining constants for the menu
    screen = configs.screen
    SCREEN_WIDTH = configs.SCREEN_WIDTH
    SCREEN_HEIGHT = configs.SCREEN_HEIGHT
    font = configs.font
    TEXT_COL = configs.TEXT_COL
    game_paused = False
    # loading btn images
    resume_img = pygame.image.load("../resources/resume.png").convert_alpha()
    quit_img = pygame.image.load("../resources/quit.png").convert_alpha()
    start_img = pygame.image.load("../resources/start.png").convert_alpha()
    pause_img = pygame.image.load("../resources/pause.png")

    # Creating Button instances
    resume_btn = button.Button((SCREEN_WIDTH/2.2), (SCREEN_HEIGHT/4), resume_img, 0.2)
    quit_btn = button.Button((SCREEN_WIDTH/2.2), (SCREEN_HEIGHT/2), quit_img, 0.2)
    start_btn = button.Button((SCREEN_WIDTH/2.2), (SCREEN_HEIGHT/4), start_img, 0.5)
    pause_btn = button.Button((SCREEN_WIDTH/1.05), (30), pause_img, 0.1)
