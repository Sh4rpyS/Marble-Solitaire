import pygame, os, json, sys
from pygame.locals import *

pygame.init()

class Sprite_Manager:
    Sprites = {}

    # Sprite loading settings
    sprite_directory = "res"
    sprite_type = ".png"
    colorkey = (0, 255, 0)

    def Get_Sprites():
        # Get the files from the directory
        files = os.listdir(Sprite_Manager.sprite_directory)

        # Filter out the wrong type files
        sprites = list(filter(lambda sprite : Sprite_Manager.sprite_type in sprite, files))

        # Get the image properties
        with open(f"{Sprite_Manager.sprite_directory}/properties.json") as f:
            properties_file = f.read()
        
        properties = json.loads(properties_file)    # Read the JSON

        # Scale and set the sprites to the dictionary
        for sprite in sprites:
            sprite_name = sprite.split(".")[0]                          # Get the sprite name
            sprite = pygame.image.load(f"{Sprite_Manager.sprite_directory}/{sprite_name}{Sprite_Manager.sprite_type}").convert()
            sprite.set_colorkey(Sprite_Manager.colorkey)                # Set the colorkey

            scale_x = properties[sprite_name][0]                        # Get the X Scale
            scale_y = properties[sprite_name][1]                        # Get the Y Scale

            sprite = pygame.transform.scale(sprite, (scale_x, scale_y)) # Change the scale

            Sprite_Manager.Sprites[sprite_name] = sprite                # Add to the dictionary

        # Debug
        #print(Sprite_Manager.Sprites)