import pygame
from load import *

nextRoom = "testRoom1"
currentRoom = "testRoom2"

if playerStats["flags"]["puzzle1"] == True:
    nextRoom = "testRoom2"
else:
    nextRoom = "testRoom"
