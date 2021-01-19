import pygame

def text(surface, text, size, (x, y), color=""):
    font = pygame.font.Font(os.path.join("..assets/fonts", "YuseiMagic-Regular.ttf"), size)
    if color == "":
        color = pygame.Color("black")
    else:
        color = color
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.x = x
    surf.blit(text_surface, (x, y))

def drawObject(Object, surface):
    obj = Object()
    obj.image.load(os.path.join(obj.image)).convert_alpha()
    obj.blit(surface, x.image, (obj.x, obj.y))