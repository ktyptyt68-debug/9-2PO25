import pygame
import math
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
dt = 0
run = True
#---config---
debug =  True
objs  =  10
#------------
class oobj:
    def __init__(self, idn):
        self.id = idn
        self.pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
objlst=[]
for i in range(1, objs):
    nobj = oobj(i)
    objlst.append(nobj)
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    screen.fill("black")
    tm = pygame.time.get_ticks()
    for i,obj in enumerate(objlst):
        obj.pos.x = (screen.get_width() / 2-200)+math.sin((tm/9000*obj.id))*10*obj.id
        obj.pos.y = (screen.get_width() / 2-200)+math.cos((tm/9000*obj.id))*10*obj.id
        pygame.draw.circle(screen, "red", obj.pos, 10)
        if debug:
            print(obj.id, obj.pos.x, obj.pos.y)
    pygame.display.flip()
    dt = clock.tick(60) / 1000
pygame.quit()