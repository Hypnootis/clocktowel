import pygame, draw

class Object(pygame.sprite.Sprite):
    def __init__(self, surf, picture=""):
        self.surf = surf
        self.image = pygame.image.load(os.path.join("../assets/sprites", self.picture)).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
    def draw():
        

class Room()

class State()

class Game()