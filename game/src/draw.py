import pygame
from classes import *
from load import *

drawablesList = []

def createDrawables(l, currentRoom, surface):
    for room in l:
        room = Object(l[room]["image"], "", 0, 0)
        drawablesList.append(room)
        #for obj in l[room]["objects"]:
        #    obj = Object(surface, l[room][obj]["image"], l[room][obj]["inspect"], l[room][obj]["x"], l[room][obj]["y"])
        #    drawablesList.append(obj)

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

def drawGame(drawablesList, surface):
    for obj in drawablesList:
        obj.draw(surface)