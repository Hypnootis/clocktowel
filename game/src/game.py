import pygame, os, json
from draw import *
from state import *

pygame.init()

SCREENW = 800
SCREENH = 600
screen = pygame.display.set_mode((SCREENW, SCREENH))
pygame.display.set_caption("Clock Towel")
clock = pygame.time.Clock()

running = True
changeRoom = False
createDrawables(rooms, currentRoom)

while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_SPACE:
                changeRoom = True
 
    
    if changeRoom == True:
        currentRoom = nextRoom
        createDrawables(rooms, currentRoom)
        changeRoom = False
    
    drawGame(drawablesList, screen)

    pygame.display.flip()
    clock.tick(60)

pygame.QUIT()