import pygame,sys
from pygame.locals import *
import numpy as np
import time

pygame.init()

#colors(RGB)
BLUE = (0,255,0)
GREEN = (0,0,255)
GREEN_army = (78,91,49)
RED = (255,0,0)
orange_sunset = (250,198,104)
BLACK = (0,0,0)
blue_light = (164,219,232)
blue_AZURE = (0,138,216)
#screen
screen= pygame.display.set_mode((1000,380))
pygame.display.set_caption("Heavy Ordnance")
screen.fill(blue_light)

#map
ocean = pygame.draw.rect(screen, blue_AZURE, (0,300,1000,80),0)
tower = pygame.draw.rect(screen,GREEN_army,(0,200,100,180),0)
sand = pygame.draw.rect(screen,orange_sunset,(100,300,100,80),0)

#canon
base = pygame.draw.rect(screen,BLACK,(35,180,25,20),0)
barrel = pygame.draw.rect(screen,BLACK,(45,160,5,20),0)






while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()




    pygame.display.update()