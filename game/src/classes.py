import pygame

class Object():
    def __init__(self, picture, inspect, x, y, typeofobject):
        self.x = x
        self.y = y
        self.picture = picture
        self.inspect = inspect
        self.image = pygame.image.load("assets/sprites/" + self.picture)
        self.rect = self.image.get_rect()
        self.type = typeofobject
    def draw(self, surf):
        surf.blit(self.image, [self.x, self.y])
    def inspect(self, inspect, surf):
        text(self.surf, self.inspect, 12, (self.x, self.y + 50), pygame.Color("black"))
        

class Pickup(Object):
    def __init__(self, picture, inspect, x, y):
        super().__init__(self, picture, inspect, x, y)
        self.dialog = True
        self.picture = picture
        self.inspect = inspect
        self.x = x
        self.y = y

class Pickup(Object):
    def __init__(self, picture, inspect, x, y):
        super().__init__(self, picture, inspect, x, y)
        self.picked = False
        self.picture = picture
        self.inspect = inspect
        self.x = x
        self.y = y

class Room(Object):
    def __init__(self, picture, inspect, x, y):
        super().__init__(self, picture, inspect, x, y)
        self.picture = picture
        self.inspect = inspect
        self.x = x
        self.y = y