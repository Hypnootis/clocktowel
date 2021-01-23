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
font = pygame.font.Font("assets/fonts/YuseiMagic-Regular.ttf", 25)
cooldown = 7000
pos = (0, 0)
text = ""
textList = {}
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

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for i in objects:
                    if i.rect.collidepoint((event.pos)) and i.type != "room":
                        break
            elif event.button == 3:
                for i in objects:
                    if i.rect.collidepoint(event.pos) and i.type != "room":
                        #textList.append(draw_text(font, i.inspectText, i.x, i.y + 20, pygame.Color("yellow")))
                        text = drawText(font, i.inspectText, i.x, i.y, pygame.Color("yellow"))
                        pos = (i.x, i.y)
                        break
    
 
    
    if changeRoom == True:
        currentRoom = nextRoom
        createDrawables(rooms, currentRoom)
        changeRoom = False
    
    screen.fill(pygame.Color("red"))
    drawGame(objects, screen)
    if text != "":
        screen.blit(text, (pos))

    pygame.display.flip()
    clock.tick(60)

pygame.QUIT
