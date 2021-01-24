import pygame
from classes import *
from load import *

#This messy function goes through the json room file, then gets the objects from the current room
#and adds them to a list

def createDrawables(l, objectl, currentRoom):
    for room in l:
        room = Object(l[currentRoom]["image"], "", 0, 0, l[currentRoom]["type"])
        objectl.append(room)
        for obj in l[currentRoom]["objects"]:
            obj = Object(l[currentRoom]["objects"][obj]["image"], l[currentRoom]["objects"][obj]["inspect"], l[currentRoom]["objects"][obj]["x"], l[currentRoom]["objects"][obj]["y"], l[currentRoom]["objects"][obj]["type"])
            objectl.append(obj)

def drawText(font, text, x, y, color=""): #Surf is the surface you want to draw the text onto, then some basic parameters like what kind of text you want to draws
    if color == "":
        color = pygame.Color("black") #If no color is specified, use black
    else:
        color = color
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.x = x
    return text_surface


#Draws all the objects in the list of drawable objects

def drawGame(objectl, surface):
    for obj in objectl:
        obj.draw(surface)