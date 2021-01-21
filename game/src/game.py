import pygame, os, json, time
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
prev_time = time.time()
dt = 0

while running:

    #Delta time
    now = time.time()
    dt = now - prev_time
    prev_time = now

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_SPACE and playerStats["flags"]["puzzle1"] == True:
                changeRoom = True
            elif event.key == pygame.K_m:
                playerStats["flags"]["puzzle1"] = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for i in objects:
                    if i.rect.collidepoint(event.pos) and i.type != "room":
                        print("Clicked!")
            elif event.button == 2:
                for i in objects:
                    if i.rect.collidepoint(event.pos) and i.type != "room":
                        i.inspect()
    
 
    
    if changeRoom == True:
        currentRoom = nextRoom
        createDrawables(rooms, currentRoom)
        changeRoom = False
    
    drawGame(objects, screen)

    pygame.display.flip()
    clock.tick(60)

pygame.QUIT()
