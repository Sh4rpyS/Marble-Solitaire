import pygame, sys
from pygame.locals import *

pygame.init()

import game, gui
from sprite import Sprite_Manager

def Init():
    global background
    background = Sprite_Manager.Sprites["background1"]

    gui.Text("title_text", "menu", 320, 180, 100, "MARBLE SOLITAIRE", (255, 255, 255), "center")
    gui.Text("version_text", "menu", 5, 620, 36, "Version 1.02", (255, 255, 255), "left")
    gui.Text("credit_text", "menu", 635, 620, 36, "Made by Veeti Tuomola", (255, 255, 255), "right")

    gui.Button("play_button", "menu", 320, 320, 200, 80, "PLAY", 42, (255, 255, 255), "center")
    gui.Button("quit_button", "menu", 320, 420, 200, 80, "QUIT", 42, (255, 255, 255), "center")

    Start()

def Input(event):
    if event.type == MOUSEBUTTONDOWN:
        if gui.Button.Buttons["play_button"].button_object.collidepoint((game.mx, game.my)):
            game.scene_game.Start()
            game.Screen.scene = "game"
        elif gui.Button.Buttons["quit_button"].button_object.collidepoint((game.mx, game.my)):
            pygame.quit()
            sys.exit()

def Start():
    pass

def Update():
    game.screen.blit(background, (0, 0))