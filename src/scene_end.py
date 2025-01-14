import pygame

import scene_game
import game, gui
from sprite import Sprite_Manager

def Init():
    global background
    background = Sprite_Manager.Sprites["background2"]

    gui.Text("win_text", "end", 320, 150, 120, "YOU WIN!", (255, 255, 255), "center")
    gui.Text("loss_text", "end", 320, 150, 120, "YOU LOST!", (255, 255, 255), "center")
    gui.Text("time_spent_text", "end", 320, 240, 42, "Time spent", (255, 255, 255), "center")

    gui.Button("play_again_button", "end", 320, 320, 200, 80, "PLAY AGAIN", 42, (255, 255, 255), "center")
    gui.Button("quit_button_2", "end", 320, 420, 200, 80, "QUIT", 42, (255, 255, 255), "center")

def Start(state):
    gui.Text.Texts["time_spent_text"].update_text(f" You spent {int(scene_game.timer)} seconds!")

    if state == 0:
        gui.Text.Texts["win_text"].set_active(False)
        gui.Text.Texts["loss_text"].set_active(True)
    elif state == 1:
        gui.Text.Texts["win_text"].set_active(True)
        gui.Text.Texts["loss_text"].set_active(False)

def Input(event):
    if event.type == pygame.MOUSEBUTTONDOWN:
        if gui.Button.Buttons["play_again_button"].button_object.collidepoint((game.mx, game.my)):
            game.scene_game.Start()
            game.Screen.scene = "game"
        elif gui.Button.Buttons["quit_button"].button_object.collidepoint((game.mx, game.my)):
            game.scene_menu.Start()
            game.Screen.scene = "menu"

def End_Game(state: int):
    game.Screen.scene = "end"
    Start(state)

def Update():
    game.screen.blit(background, (0, 0))