import pygame #Some cool imports
import sys
import os
import random


pygame.init()

clock = pygame.time.Clock()
screen_width = 800
screen_length = 600


screen = pygame.display.set_mode((screen_width, screen_length)) #Setting the game window
pygame.display.set_caption("Testing") #Title for the game window

running = True

class Object():
    def __init__(self):
        self.image = pygame.image.load("assets/sprites/example.png")
    def draw(self, surface):
        self.blit(surface, self.image, (self.x, self.y))

lista = []
paska = Object()

while running:
    
    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

    screen.fill(pygame.Color("cornflowerblue"))
    paska.draw(screen)

    pygame.display.flip()
    clock.tick(60)


pygame.QUIT()