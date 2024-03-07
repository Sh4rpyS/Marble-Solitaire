import pygame, sys, win32gui, win32con
from pygame.locals import *

pygame.init()

import sprite, gui
import scene_game, scene_end, scene_menu

class Screen:
    width = 640
    height = 640
    title = "Marble Solitaire"
    fps = 60

    scene = "menu"
    bg_color = (0, 0, 0)

def Init() -> None:
    # Console
    if True:
        hide = win32gui.GetForegroundWindow()
        win32gui.ShowWindow(hide , win32con.SW_HIDE)
        
    global screen, clock
    screen = pygame.display.set_mode((Screen.width, Screen.height), 0, 32)
    pygame.display.set_caption(Screen.title)
    clock = pygame.time.Clock()

    global get_ticks_last_frame
    get_ticks_last_frame = 0


def Start() -> None:
    sprite.Sprite_Manager.Get_Sprites()
    scene_menu.Init()
    scene_game.Init()
    scene_end.Init()

    while 1: Update()

def Stop() -> None:
    pygame.quit()
    sys.exit()

def Count_Delta_Time() -> None:
    global delta_time, get_ticks_last_frame, ticks
    ticks = pygame.time.get_ticks()
    delta_time = (ticks - get_ticks_last_frame) / 1000.0
    get_ticks_last_frame = ticks

def Input() -> None:
    global mx, my
    mx, my = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == QUIT: Stop()

        # Scene specific input
        if Screen.scene == "menu":
            scene_menu.Input(event)
        elif Screen.scene == "game":
            scene_game.Input(event)
        elif Screen.scene == "end":
            scene_end.Input(event)

        # Scene switching
        if event.type == KEYDOWN:
            if event.key == K_1:
                scene_menu.Start()
                Screen.scene = "menu"
            if event.key == K_2:
                scene_game.Start()
                Screen.scene = "game"
            if event.key == K_3:
                scene_end.End_Game(0)
            if event.key == K_4:
                scene_end.End_Game(1)
        


def Update() -> None:
    clock.tick(Screen.fps)
    Count_Delta_Time()
    Input()

    # Might not even need this, because we are using a background
    # So it is disabled to improve performance
    screen.fill(Screen.bg_color)

    if Screen.scene == "menu":
        scene_menu.Update()
    elif Screen.scene == "game":
        scene_game.Update()
    elif Screen.scene == "end":
        scene_end.Update()
    
    gui.Button.Draw()
    gui.Text.Draw()

    pygame.display.update()
    pygame.display.set_caption(f"{Screen.title} | {int(clock.get_fps())} FPS")