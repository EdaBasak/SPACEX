import pygame
import sys
import math
import random
from  threading import Timer
from Bullet import Bullet
from spaceStone import spaceStone
from spaceShip import spaceShip
from TargetOne import TargetOne
from pTimer import  pTimer
class ChapterOne():

        def __init__(self, screen):
            self.name = "Space X"
            self.spaceShip = spaceShip(screen)
            self.targets = []
            self.backGroundImage = pygame.transform.scale(pygame.image.load("images/BG.png"),
                                                          (screen.get_width(), screen.get_height()))
            self.backGroundImageX = 0
            self.backGroundImageY = 0
            self.backGroundImageY2 = -screen.get_height()
            self.screen = screen

            # 2 saniyede bir hedef üretilmeli
            # bunun için kendi yazdığımız timer sınıfını kulllıyoruz
            # bu işlem için uygun olan threadlerdir ancak bu konuya sonra geleceğiz
            self.pgenerateTargetTimer = pTimer(2, self.generateTarget, screen)

            self.finishEvent = pygame.event.Event(pygame.USEREVENT, attr1='finishEvent')

        def start(self, screen):

            self.pgenerateTargetTimer.start()

        def finish(self, screen):
            self.pgenerateTargetTimer.stop()
            pygame.event.post(self.finishEvent)

        def generateTarget(self, arguments):
            newTarget = TargetOne(arguments[0])
            self.targets.append(newTarget)

        def drawBackGround(self, screen):
            self.backGroundImageY = self.backGroundImageY + 1
            self.backGroundImageY2 = self.backGroundImageY2 + 1
            screen.blit(self.backGroundImage, (0,self.backGroundImageY2))
            screen.blit(self.backGroundImage, (0,self.backGroundImageY))
            if (self.backGroundImageY == screen.get_height()):
                self.backGroundImageY = -screen.get_height()
            if (self.backGroundImageY2 == screen.get_height()):
                self.backGroundImageY2 = -screen.get_height()
        def drawShip(self, screen):
            self.spaceShip.draw(screen)





        def drawTargets(self, screen):
            for target in self.targets:
                exposed = target.draw(screen)
                if exposed:
                    self.targets.remove(target)
                    pygame.event.post(spaceStone.ExposedEvent)
                    if self.spaceShip.exposed:
                        pygame.event.post(self.spaceShip.exposedEvent)
                        self.finish(screen)

                else:
                    if target.rectangle.colliderect(self.spaceShip.rectangle):
                        if not target.exposed:
                            target.expose()
                            self.spaceShip.expose()

                    else:
                        for bullet in self.spaceShip.bullets:
                            # eğer eşleşme varsa
                            if target.rectangle.colliderect(bullet.rectangle):
                                # target hit almış demektir.
                                target.hit()
                                # mermi kaybolmalı
                                self.spaceShip.bullets.remove(bullet)

        def draw(self, screen):
            self.drawBackGround(screen)
            self.drawShip(screen)
            self.drawTargets(screen)