import pygame,sys
from pygame.locals import *

pygame.init()
DISPLAYSURF= pygame.display.set_mode((1000,380))
pygame.display.set_caption("Heavy Ordnance")
RED = (255,0,0)
BLACK = (0,0,0)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()




    pygame.display.update()