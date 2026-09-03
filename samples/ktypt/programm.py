import pygame
import math
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)
dgfont = pygame.font.Font(None, 16)
dt = 0
run = True
flowcs = False
pan = False
pan_x = 0
pan_y = 0
cm_x = 0
cm_y = 0
cm_start_x = 0
cm_start_y = 0
cm_vel_x = 0
cm_vel_y = 0
lst_mouse_pos = (0,0)
#---config---
debug =  False
objs  =  100
#------------
class oobj:
    def __init__(self, idn):
        self.id = idn
        self.pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
        self.vel = pygame.Vector2(0, 0)
        self.base_x = screen.get_width() / 2
        self.base_y = screen.get_height() / 2
objlst=[]
for i in range(1, objs):
    nobj = oobj(i)
    objlst.append(nobj)
while run:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                flowcs = True
            if event.button == 3:
                pan = True
                mspos = pygame.mouse.get_pos()
                pan_x = mspos[0]
                pan_y = mspos[1]
                cm_start_x = cm_x
                cm_start_y = cm_y
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                flowcs = False
            if event.button == 3:
                pan = False
        if event.type == pygame.QUIT:
            run = False
    screen.fill("black")
    mspos = pygame.mouse.get_pos()
    if pan:
        dx = mspos[0] - pan_x
        dy = mspos[1] - pan_y
        cm_x = cm_start_x + dx
        cm_y = cm_start_y + dy
        cm_vel_x = dx * 0.1
        cm_vel_y = dy * 0.1
        text_surface = font.render(f"cm_x: {cm_x}, cm_y: {cm_y}", True, "white")
        screen.blit(text_surface, (0, 0))
    else:
        cm_x += cm_vel_x
        cm_y += cm_vel_y
        cm_vel_x *= 0.95
        cm_vel_y *= 0.95
    tm = pygame.time.get_ticks()
    for i,obj in enumerate(objlst):
        t = tm / 1000 + obj.id
        if flowcs:
            tx, ty = mspos[0] - cm_x, mspos[1] - cm_y
        else:
            tx = obj.base_x + math.sin(t) * 10*obj.id
            ty = obj.base_y + math.cos(t) * 10*obj.id
        obj.vel.x += (tx - obj.pos.x) * 0.1
        obj.vel.y += (ty - obj.pos.y) * 0.1
        obj.vel *= 0.95
        obj.pos += obj.vel
        for j in range(i+1, len(objlst)):
            d = obj.pos.distance_to(objlst[j].pos)
            if d < 50 and d>0:
                nx = (objlst[j].pos.x - obj.pos.x) / d
                ny = (objlst[j].pos.y - obj.pos.y) / d
                obj.vel.x -= nx *2
                obj.vel.y -= ny *2
                objlst[j].vel.x += nx *2
                objlst[j].vel.y += ny *2
        pygame.draw.circle(screen, "red", (obj.pos.x+cm_x, obj.pos.y+cm_y), 10)
        if debug:
            text_surface1 = dgfont.render(f"id: {obj.id}, pos: ({obj.pos.x}, {obj.pos.y})", True, "white")
            screen.blit(text_surface1, (obj.pos.x+cm_x, obj.pos.y+cm_y))
    pygame.display.flip()
    dt = clock.tick(30) / 1000
pygame.quit()