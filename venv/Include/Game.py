#çizim ile işlemler yapabilsek dahi kontrol için objelere ihtiyacımız vardır.
#bu noktada object merkezli programlama yapmamız gerekir.
import pygame
import sys
import math
import random
from Chapter import ChapterOne
from Menu import Menu
from TargetOne import TargetOne
pygame.init()
gameDisplay_width=800
gameDisplay_height=600
gameDisplay = pygame.display.set_mode((gameDisplay_width,gameDisplay_height))
pygame.display.set_caption('Space X')

crashed = False
clock = pygame.time.Clock()
chapter= ChapterOne(gameDisplay)
chapter.start(gameDisplay)
endEvent=pygame.event.Event(pygame.USEREVENT, attr1='endEvent')

menu=Menu(gameDisplay.get_rect())


end=False
while not crashed:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            crashed = True
        elif event.type == pygame.KEYDOWN:
            if event.key==pygame.K_ESCAPE:
                chapter.pgenerateTargetTimer.pause(True)
                crashed=menu.runMenu(gameDisplay)
                chapter.pgenerateTargetTimer.pause(False)

            if event.key == pygame.K_UP:
                chapter.spaceShip.my=-1
            if event.key == pygame.K_DOWN:
                chapter.spaceShip.my=1
            if event.key == pygame.K_LEFT:
                chapter.spaceShip.mx=-1
            if event.key == pygame.K_RIGHT:
                chapter.spaceShip.mx=1
            if event.key == pygame.K_SPACE:
                chapter.spaceShip.fire(gameDisplay)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                chapter.spaceShip.my=0
            if event.key == pygame.K_DOWN:
                chapter.spaceShip.my=0
            if event.key == pygame.K_LEFT:
                chapter.spaceShip.mx=0
            if event.key == pygame.K_RIGHT:
                chapter.spaceShip.mx=0
        #event karşılaştırmalarında eşitlik koşulu çalışır
        #eventlar aynı olmalı özellikleriyle birlikte
        elif event== chapter.finishEvent:
            print(event)
            end=True

        elif event== chapter.spaceShip.exposedEvent:
            print(event)

    if not end:
        chapter.draw(gameDisplay)


    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()


