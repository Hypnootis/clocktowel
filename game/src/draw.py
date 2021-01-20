import pygame
from classes import *
from load import *

drawablesList = []

#This messy function goes through the json room file, then gets the objects from the current room
#and adds them to a list

def createDrawables(l, currentRoom):
    for room in l:
        room = Object(l[currentRoom]["image"], "", 0, 0)
        drawablesList.append(room)
        for obj in l[currentRoom]["objects"]:
            obj = Object(l[currentRoom]["objects"][obj]["image"], l[currentRoom]["objects"][obj]["inspect"], l[currentRoom]["objects"][obj]["x"], l[currentRoom]["objects"][obj]["y"])
            drawablesList.append(obj)

def text(surface, text, size, x, y, color=""):
    font = pygame.font.Font(os.path.join("..assets/fonts", "YuseiMagic-Regular.ttf"), size)
    if color == "":
        color = pygame.Color("black")
    else:
        color = color
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.x = x
    surf.blit(text_surface, (x, y))

#Draws all the objects in the list of drawable objects

def drawGame(drawablesList, surface):
    for obj in drawablesList:
        obj.draw(surface)