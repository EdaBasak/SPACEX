#çizim ile işlemler yapabilsek dahi kontrol için objelere ihtiyacımız vardır.
#bu noktada object merkezli programlama yapmamız gerekir.
import pygame
import sys
import math
import random
from Chapter import ChapterOne
from Menu import Menu
from TargetOne import TargetOne
from TargetTwo import TargetTwo
from TargetTree import TargetTree
from Plane import *
from ScoreBoard import *
pygame.init()

gameDisplay_width=800
gameDisplay_height=600
gameDisplay = pygame.display.set_mode((gameDisplay_width,gameDisplay_height))
pygame.display.set_caption('SPACE X')

crashed = False

clock = pygame.time.Clock()
chapter= ChapterOne(gameDisplay)
chapter.start(gameDisplay)
endEvent=pygame.event.Event(pygame.USEREVENT, attr1='endEvent')

menu=Menu(gameDisplay.get_rect())
end=False
ScoreBoard.init_ScoreBoard()
ScoreBoard.set_Score()
while not crashed:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            crashed = True
        elif event.type == pygame.KEYDOWN:
            if event.key==pygame.K_ESCAPE:
                chapter.pgenerateTargetTimer.pause(True)
                crashed=menu.runMenu(gameDisplay)
                chapter.pgenerateTargetTimer.pause(False)


        elif event.type == pygame.MOUSEBUTTONDOWN:
            chapter.plane.fire(gameDisplay,pygame.mouse.get_pos())
        #event karşılaştırmalarında eşitlik koşulu çalışır
        #eventlar aynı olmalı özellikleriyle birlikte
        elif event== chapter.finishEvent:
            print(event)

            end=True

        elif event== chapter.plane.exposedEvent:
            print(event)
        elif event == TargetOne.ExposedEvent:
            ScoreBoard.set_Score(1)
        elif event == TargetTwo.ExposedEvent:
            ScoreBoard.set_Score(5)
        elif event == TargetTree.ExposedEvent:
            ScoreBoard.set_Score(10)

    if not end:
        mouse_position = pygame.mouse.get_pos()
        chapter.draw(gameDisplay,mouse_position)
        ScoreBoard.draw(gameDisplay)


    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()

