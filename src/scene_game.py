import sys, pygame
from pygame.locals import *
pygame.init()

import game, gui
import objects
from sprite import Sprite_Manager

def Init():

    # Gets the background sprite
    global background
    background = Sprite_Manager.Sprites["background"]

    gui.Button("menu_button", "game", 5, 30, 100, 50, "EXIT", 42, (255, 255, 255), "left")
    gui.Button("start_button", "game", 5, 85, 100, 50, "START", 42, (255, 255, 255), "left")

    gui.Text("timer_header_text", "game", 540, 20, 32, "TIME", (255, 255, 255), "center")
    gui.Text("timer_text", "game", 540, 60, 52, "NOT STARTED", (255, 255, 255), "center")

    Start()

def Start():

    global timer, timer_running
    timer_running = False
    timer = 0
    
    gui.Button.Buttons["start_button"].set_active(True)
    gui.Text.Texts["start_button_text"].set_active(True)

    gui.Text.Texts["timer_text"].update_text("NOT STARTED")

    # Clear objects
    objects.Hole.Holes.clear()
    objects.Marble.Marbles.clear()

    # Create holes
    for hole in objects.Hole.Tiles:
        objects.Hole(hole[0], hole[1])

    # Create marbles
    for hole in objects.Hole.Holes.values():
        hole.Set_Marble(objects.Marble())

def Input(event):
    global timer_running, timer, timer_thread

    if event.type == MOUSEBUTTONDOWN:
        objects.Marble.Select_Marble()          # Checks if you select a marble

        if gui.Button.Buttons["start_button"].button_object.collidepoint((game.mx, game.my)) and gui.Button.Buttons["start_button"].active:
            gui.Text.Texts["timer_text"].update_text("0s")
            objects.Hole.Holes[(3, 3)].marble.remove()
            gui.Button.Buttons["start_button"].set_active(False)
            gui.Text.Texts["start_button_text"].set_active(False)

            timer_running = True
        elif gui.Button.Buttons["menu_button"].button_object.collidepoint((game.mx, game.my)):
            game.scene_menu.Start()

            timer_running = False
            timer = 0

            game.Screen.scene = "menu"

    if event.type == KEYDOWN:
        if event.key == K_r:
            if objects.Marble.Selected != None: objects.Marble.Selected.remove()

def Update():
    global timer
    # Draws the background for the game
    game.screen.blit(background, (0, 0))

    # Update the timer
    if timer_running:
        timer += game.delta_time
        gui.Text.Texts["timer_text"].update_text(f"{int(timer)}s")

    # Draws holes
    objects.Hole.Draw()
    objects.Marble.Draw()