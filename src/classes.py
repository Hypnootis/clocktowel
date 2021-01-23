import pygame

class Object():
    def __init__(self, picture, inspectText, x, y, typeofobject):
        self.x = x
        self.y = y
        self.picture = picture
        self.inspectText = inspectText
        self.image = pygame.image.load("assets/sprites/" + self.picture)
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        self.type = typeofobject
    def draw(self, surf):
        surf.blit(self.image, [self.x, self.y])
        

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
    def __init__(self, picture, inspect, x, y, typeofobject):
        super().__init__(self, picture, inspect, x, y, typeofobject)
        self.picture = picture
        self.inspect = inspect
        self.x = x
        self.y = y
        self.type = typeofobject
