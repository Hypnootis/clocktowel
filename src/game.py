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
objects = []
createDrawables(rooms, objects, currentRoom)
dt = 0
font = pygame.font.Font("assets/fonts/YuseiMagic-Regular.ttf", 20)
cooldown = 5000
pos = (0, 0)
text = ""
textList = []
textPosList = []

while running:
    oldtime = 0
    

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_SPACE and playerStats["flags"]["puzzle1"] == True:
                changeRoom = True
            elif event.key == pygame.K_m:
                playerStats["flags"]["puzzle1"] = True
            elif event.key == pygame.K_f:
                playerStats["flags"]["puzzle1"] = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for i in objects:
                    if i.rect.collidepoint((event.pos)) and i.type != "room":
                        break
            elif event.button == 3:
                for i in objects: #This is so dirty, but I could not think of a better way right now
                    if i.rect.collidepoint(event.pos) and i.type != "room":
                        oldTime = pygame.time.get_ticks() #Each inspect text should have their own timer rather than varying on just one
                        text = drawText(font, i.inspectText, i.x, i.y, pygame.Color("yellow"))
                        textPos = (i.x, i.y)
                        if text not in textList and textPos not in textPosList: #Two lists that store text_surface Object and coordinates
                            textList.append(text)
                            textPosList.append((i.x, i.y))
                        break
    
 
    
    drawGame(objects, screen) #Drawing seems a bit glitchy, but works for the most part, except on rare occasions?
    screen.blit(drawText(font, "changeRoom is: " + str(changeRoom), 0, 0), (0, 0))

    if changeRoom == True:
        currentRoom = nextRoom
        objects = []
        createDrawables(rooms, objects, currentRoom)
        textList = []
        textPosList = []
        changeRoom = False
        

    #This handles drawing and un-drawing of text when inspected
    if len(textList) > 0:
        for i in range(len(textList)):
            screen.blit(textList[i], (textPosList[i][0] - 50, textPosList[i][1] - 30)) #Offset for text is hardcoded, and doesn't have any boundaries
            newTime = pygame.time.get_ticks()
            if newTime - oldTime >= cooldown: #Probably a dirty way of doing this
                oldTime = newTime #Each time a text surface gets deleted the timer resets, caused by the break but can't fix it rn
                for j in textList:
                    textPosList.pop(textList.index(j))
                    textList.remove(j)
                break

    pygame.display.flip()
    clock.tick(60)

pygame.QUIT