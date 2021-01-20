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
clicked = []

while running:
    mousePos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_SPACE and playerStats["flags"]["puzzle1"] == True:
                changeRoom = True
            elif event.key == pygame.K_m:
                playerStats["flags"]["puzzle1"] = True
        elif event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
            print("clicked!")
            for s in objects:
                if s.rect.collidepoint(mousePos) and s.type != "room":
                    clicked.append(s)
        elif event.type == pygame.MOUSEBUTTONUP:
            clicked = []
    
    if clicked != []:
        print(clicked)
                
 
    
    if changeRoom == True:
        currentRoom = nextRoom
        createDrawables(rooms, currentRoom)
        changeRoom = False
    
    drawGame(objects, screen)

    pygame.display.flip()
    clock.tick(60)

pygame.QUIT()
