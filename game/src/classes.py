import pygame

class Object():
    def __init__(self, picture, inspect, x, y):
        self.x = x
        self.y = y
        self.picture = picture
        self.inspect = inspect
        self.image = pygame.image.load("assets/sprites/" + self.picture)
    def draw(self, surf):
        surf.blit(self.image, [self.x, self.y])
    #def inspect(self, inspect, surf):
        #text(self.surf, self.inspect, 12, (self.x, self.y + 50), pygame.Color("black"))
        

class Npc(Object):
    def __init__(self):
        self.dialog = True

class Pickup(Object):
    def __init__(self):
        self.picked = False

class Room(Object):
    def __init__(self, picture, inspect, x, y):
        super().__init__(self, picture, inspect, x, y)
        self.picture = picture
        self.inspect = inspect
        self.x = x
        self.y = y