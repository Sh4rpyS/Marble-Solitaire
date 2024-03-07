import pygame, sys
from pygame.locals import *
from sprite import Sprite_Manager

import game
import scene_end, scene_game

class Marble:
    Marbles = []                                                        # Stores all the marbles
    Selected = None                                                     # Selected marble
    Possible_Moves = []                                                 # Stores possible moves

    def __init__(self):
        self.sprite = Sprite_Manager.Sprites["marble"]                  # Gets the sprite
        self.size = self.sprite.get_width()                             # Gets the size
        self.object = game.screen.blit(self.sprite, (-100, -100))
        self.hole = None

        Marble.Marbles.append(self)                                     # Adds itself to the list

    def remove(self):                                                   # Removes the marble from
        Marble.Marbles.remove(self)
        self.hole.marble = None
        Marble.Selected = None

    def draw(self):
        if self.hole != None:
            if Marble.Selected == self:
                pygame.draw.circle(game.screen, (255, 0, 0), (self.hole.x + self.size / 2, self.hole.y + self.size / 2), self.size / 1.5)

            self.object = game.screen.blit(self.sprite, (self.hole.x, self.hole.y))   # Draws the object

    def Draw():
        for marble in Marble.Marbles:
            marble.draw()

        if Marble.Selected != None and len(Marble.Possible_Moves) == 0:
            Marble.Check_For_Moves(Marble.Selected)

    def Select_Marble():

        if Marble.Selected != None:
            for hole in Hole.Holes.items():
                if hole[1] in Marble.Possible_Moves:
                    if hole[1].object.collidepoint((game.mx, game.my)):
                        Marble.Move(hole)
                        break

        # Checks if you are clicking on a marble
        # If the same marble is not selected, mark it selected
        # Otherwise deselect it

        for marble in Marble.Marbles:
            if marble.object.collidepoint((game.mx, game.my)):
                Marble.Possible_Moves.clear()
                if Marble.Selected != marble: Marble.Selected = marble
                else: Marble.Selected = None
                    
                break

    def Move(selection: "Hole"):
        # Remove the meddle marble
        tile0 = (selection[1].x_tile, selection[1].y_tile)
        tile1 = (Marble.Selected.hole.x_tile, Marble.Selected.hole.y_tile)
        middle_tile = ((tile0[0] + tile1[0]) // 2, (tile0[1] + tile1[1]) // 2)

        # Make the move itself
        Marble.Selected.hole.marble = None
        Marble.Possible_Moves.clear()
        selection[1].Set_Marble(Marble.Selected)

        Hole.Holes[middle_tile].marble.remove() # Removes the one marble

        # Check if a win or a loss happens
        Marble.Check_For_End()

        Marble.Possible_Moves.clear()

    def Check_For_Moves(selected):
        hole = selected.hole
        h_x = hole.x_tile
        h_y = hole.y_tile

        moves = [(h_x, h_y - 2), (h_x, h_y + 2), (h_x - 2, h_y), (h_x + 2, h_y)]
        
        for move in moves:
            if move in Hole.Holes.keys():
                if Hole.Holes[move].marble == None:
                    tile0 = move
                    tile1 = (selected.hole.x_tile, selected.hole.y_tile)
                    middle_tile = ((tile0[0] + tile1[0]) // 2, (tile0[1] + tile1[1]) // 2)

                    if Hole.Holes[middle_tile].marble != None:
                        Marble.Possible_Moves.append(Hole.Holes[move])

    # Checks if a win or a loss happens
    def Check_For_End():
        if len(Marble.Marbles) <= 1:
            if Hole.Holes[(3, 3)].marble != None:
                scene_end.End_Game(1)
                scene_game.timer_running = False
            else:
                scene_end.End_Game(0)
                scene_game.timer_running = False
        else:
            for marble in Marble.Marbles:
                Marble.Check_For_Moves(marble)

            if len(Marble.Possible_Moves) == 0:
                scene_end.End_Game(0)
                scene_game.timer_running = False

class Hole:
    # Game layout
    Tiles = [
        (2, 0), (3, 0), (4, 0),
        (2, 1), (3, 1), (4, 1),
        (0, 2), (1, 2), (2, 2), (3, 2), (4, 2), (5, 2), (6, 2),
        (0, 3), (1, 3), (2, 3), (3, 3), (4, 3), (5, 3), (6, 3),
        (0, 4), (1, 4), (2, 4), (3, 4), (4, 4), (5, 4), (6, 4),
        (2, 5), (3, 5), (4, 5),
        (2, 6), (3, 6), (4, 6)
    ]

    Holes = {}      # Stores all the holes

    def __init__(self, x_tile: int, y_tile: int) -> None:
        self.x_tile = x_tile                                 # Tile position in the x-axis
        self.y_tile = y_tile                                 # Tile position in the y-axis
        
        self.sprite = Sprite_Manager.Sprites["hole"]         # Get the sprite
        self.object = game.screen.blit(self.sprite, (-100, -100))  # Draw the hole

        self.size = self.sprite.get_width()                  # The sprite is a square
        self.x = self.size / 2 + (128 / 6) * self.x_tile + self.size * self.x_tile
        self.y = self.size / 2 + (128 / 6) * self.y_tile + self.size * self.y_tile

        self.marble = None

        self.highlight = pygame.Surface((self.size / 0.65625, self.size / 0.65625))
        self.highlight.set_colorkey((0, 0, 0))
        pygame.draw.circle(self.highlight, (255, 255, 255), (self.highlight.get_width() / 2, self.highlight.get_width() / 2), self.size / 1.5)
        self.highlight.set_alpha(80)

        Hole.Holes[(self.x_tile, self.y_tile)] = self        # Add itself to the list

    def draw(self):
        self.object = game.screen.blit(self.sprite, (self.x, self.y))  # Draw the hole

    def Set_Marble(self, marble: Marble):
        if self.marble == None:
            self.marble = marble                             # Change marble if possible
            self.marble.hole = self                          # Set the hole for the marble

    def Draw():
        for hole in Hole.Holes.values():
            hole.draw()

            if hole in Marble.Possible_Moves:
                x = hole.x - (hole.highlight.get_width() - hole.size) / 2 + 1
                y = hole.y - (hole.highlight.get_width() - hole.size) / 2 + 1

                game.screen.blit(hole.highlight, (x, y))

            if not hole.marble == None:
                if not hole.marble in Marble.Marbles:
                    hole.marble = None
                    break
