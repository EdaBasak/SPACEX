import pygame
import sys
import math
import random
from  threading import Timer
from TargetOne import TargetOne
from TargetTwo import TargetTwo
from TargetTree import TargetTree
from Plane import Plane
from Bullet import Bullet
from pTimer import  pTimer
from ScoreBoard import ScoreBoard

score=0
pygame.font.init()
score_font = pygame.font.Font(None, 27)
score_numb_font = pygame.font.Font(None, 27)
score_msg = score_font.render("Bullet Number:", 1, pygame.Color("Purple"))
score_msg_size = score_font.size("Bullet Number")
tim_font=pygame.font.Font(None, 27)
tim_msg=tim_font.render("Timer:",1,pygame.Color("Purple"))
tim_msg_size=tim_font.size("timer")




class ChapterOne():

    def __init__(self, screen):
        self.name = "Space X"
        self.plane = Plane(screen)
        self.targets = []
        self.backGroundImage = pygame.transform.scale(pygame.image.load("images/png/BG.png"),
                                                      (screen.get_width(), screen.get_height()))
        self.backGroundImageX = 0
        self.backGroundImageY = 0
        self.backGroundImageY2 = -screen.get_height()
        self.screen = screen
        width = screen.get_width()
        height = screen.get_height()
        self.x = width / 2
        self.y = height / 2
        self.flyImages = [pygame.transform.scale(pygame.image.load("images/spaceship13.png"), (100, 100))]
        self.rectangle = self.flyImages[0].get_rect(center=(self.x, self.y))
        self.exposedImage = pygame.transform.scale(pygame.image.load("images/gameover2.png"),
                                              (self.rectangle[1], self.rectangle[2]))


        self.exposed = False
        self.exposedEvent = pygame.event.Event(pygame.USEREVENT, attr1='planeExposedEvent')
        self.time=100

        self.targetOrder = 0;
        # 2 saniyede bir hedef üretilmeli
        # bunun için kendi yazdığımız timer sınıfını kulllıyoruz

        self.pgenerateTargetTimer = pTimer(2, self.generateTarget, screen)
        self.tim = pTimer(1, self.decreaseTimer, screen)

        self.finishEvent = pygame.event.Event(pygame.USEREVENT, attr1='finishEvent')

    def start(self, screen):

        self.pgenerateTargetTimer.start()
        self.tim.start()
    def finish(self, screen):
        self.pgenerateTargetTimer.stop()

        pygame.event.post(self.finishEvent)

        self.tim.stop()
    def generateTarget(self, arguments):
        #arguments[0]olmalı
        if self.targetOrder%3 == 0:
            newTarget = TargetOne(arguments[0])
            self.targets.append(newTarget)
        elif  self.targetOrder%3 == 1:
            newTarget2=TargetTwo(arguments[0])
            self.targets.append(newTarget2)
        elif self.targetOrder%3==2:
            newTarget3=TargetTree(arguments[0])
            self.targets.append(newTarget3)

        self.targetOrder += 1
    #arka planı yukardan aşağıya akacak şekilde çizdiriyoruz.
    def drawBackGround(self, screen):
        self.backGroundImageY = self.backGroundImageY + 1
        self.backGroundImageY2 = self.backGroundImageY2 + 1
        screen.blit(self.backGroundImage, (0, self.backGroundImageY2))
        screen.blit(self.backGroundImage, (0, self.backGroundImageY))
        if (self.backGroundImageY == screen.get_height()):
            self.backGroundImageY = -screen.get_height()
        if (self.backGroundImageY2 == screen.get_height()):
            self.backGroundImageY2 = -screen.get_height()
    #uzay gemimizi çizdiriyoruz
    def drawPlane(self, screen,mousepos):
        self.plane.draw2(screen,mousepos)
    #uzay gemimizden çıkacak mermileleri çizdiriyoruz
    def drawBulletNumber(self, screen, bulletNumber):
        score_numb = score_numb_font.render(str(bulletNumber), 1, pygame.Color("Purple"))
        screen.blit(score_msg, (screen.get_width() - score_msg_size[0] - 60, 10))
        screen.blit(score_numb, (screen.get_width() - 45, 10))
        #Projemizde bulunan geri sayacı burada yazdırıyoruz
    def drawTimer(self, screen):
        tim_numb = tim_font.render(str(self.time), 1, pygame.Color("Purple"))
        screen.blit(tim_msg, (screen.get_width() - tim_msg_size[0] - 60, 40))
        screen.blit(tim_numb, (screen.get_width() - 45,40))

    #Zamanı burada azaltıyoruz
    def decreaseTimer(self, screen):
        self.time=self.time-1


    def drawTargets(self, screen):
        for target in self.targets:
            exposed = target.draw(screen)
            if exposed:
                self.targets.remove(target)
                if self.plane.exposed:
                    pygame.event.post(self.plane.exposedEvent)
                    self.finish(screen)
            else:
                if target.rectangle.colliderect(self.plane.rectangle):
                    if not target.exposed:
                        target.expose()
                        self.plane.expose()

                else:
                    for bullet in self.plane.bullets:
                        # eğer eşleşme varsa
                        if target.rectangle.colliderect(bullet.rectangle):
                            # target hit almış demektir. Eğer hedef öldüyse planenin mermi sayısını artıırmak için plane nesnesini hit metodu içinde gönderiyoruz
                            target.hit(self.plane)
                            # mermi kaybolmalı
                            self.plane.bullets.remove(bullet)


    #Oyunu çizdiriyoruz
    def draw(self, screen,mousepos):
        self.drawBackGround(screen)
        self.drawPlane(screen,mousepos)
        self.drawPlane(screen,mousepos)
        self.drawTargets(screen)
        if self.plane.bulletNumber<=0:
            pygame.event.post(self.finishEvent)
            screen.blit(self.exposedImage, self.rectangle)
        if self.time <= 0:
            screen.blit(self.exposedImage, self.rectangle)


            pygame.event.post(self.finishEvent)



        self.drawBulletNumber(screen, self.plane.bulletNumber)
        self.drawTimer(screen)


