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
dt = 0
font = pygame.font.Font("assets/fonts/YuseiMagic-Regular.ttf", 20)
cooldown = 7000
pos = (0, 0)
text = ""
textList = []
textPosList = []

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
                for i in objects: #This is so dirty, but I could not think of a better way right now
                    if i.rect.collidepoint(event.pos) and i.type != "room":
                        text = drawText(font, i.inspectText, i.x, i.y, pygame.Color("yellow"))
                        textPos = (i.x, i.y)
                        if text not in textList and textPos not in textPosList: #I have two lists that store text_surface Object and coordinates
                            textList.append(text)
                            textPosList.append((i.x, i.y))
                        break
    
 
    
    if changeRoom == True:
        currentRoom = nextRoom
        createDrawables(rooms, currentRoom)
        textList = []
        changeRoom = False
    
    screen.fill(pygame.Color("red"))
    drawGame(objects, screen) #Abstracted my blits to this, look at draw.py for details


    for i in range(len(textList)):
        screen.blit(textList[i], (textPosList[i][0] - 50, textPosList[i][1] - 30)) #Offset is hardcoded, and doesn't have any boundaries

    pygame.display.flip()
    clock.tick(60)

pygame.QUIT
