import pygame
from pygame.math import Vector2
import sys
import math
import random

from Bullet import Bullet
class Plane():
    def __init__(self,screen):
        #Başlangıçta 20 mermiyle başlıyoruz
        self.bulletNumber = 20
        width=screen.get_width()
        height=screen.get_height()
        self.x = width/2
        self.y = height /2

        
        self.shootImageOrder=0
        self.flyImages=[pygame.transform.scale(pygame.image.load("images/spaceship13.png"), (100, 100))]
        self.rectangle = self.flyImages[0].get_rect(center=(self.x,self.y))
        self.rectangle.centerx=self.x
        self.rectangle.centery=self.y
        self.pos = Vector2((self.x,self.y))
        #Oyun bittiğide açılacak ulan game over resmini burada ayarlıyoruz
        self.bullets = []
        self.exposedImage=pygame.transform.scale(pygame.image.load("images/gameover2.png"), (self.rectangle[1], self.rectangle[2]))


        self.exposed=False
        self.exposedEvent=pygame.event.Event(pygame.USEREVENT, attr1='planeExposedEvent')





    def draw(self,screen):
        if self.exposed:
            screen.blit(self.exposedImage, self.rectangle)
            return True

        self.rectangle[0]=self.x-112
        self.rectangle[1]=self.y-75
        self.rectangle.clamp_ip(screen.get_rect())# plane objesini ekran karesi içinde tutar
        screen.blit(self.flyImages[0], self.rectangle)
        for bullet in self.bullets:
            bullet.draw(screen)
            #rectangle sınıfının contains fonsiyonu dörtgenin diğerinin içinde olup olmadığı bilgisini döndürür.
            #biz burada mermiler ekrandan çıkmışmı kontrolü yapacağız
            #ekrandan çıkan mermiler mermi listesinden silinmeli, aksi taktirde binlerce mermi sonsuzluğa kadar gider bu da boşa kaynak sarfıdır.
            if not screen.get_rect().contains(bullet.rectangle):
                self.bullets.remove(bullet) #foreach döngülerinde bunu yapmak iyi bir yöntem değildir, çünkü dizin bozulur. Bir çok programlama dilinde hata alırsınız.
                                            #ancak burada python kabul etti :D

    def draw2(self,screen,mposition):
        if self.exposed:
            screen.blit(self.exposedImage, self.rectangle)
            return True
        image = self.flyImages[0]
        direction = mposition -self.pos
        radius,angle = direction.as_polar()
        image = pygame.transform.rotate(image, -angle-90)
        screen.blit(image, self.rectangle)

        for bullet in self.bullets:
            bullet.draw(screen)
            # rectangle sınıfının contains fonsiyonu dörtgenin diğerinin içinde olup olmadığı bilgisini döndürür.
            # biz burada mermiler ekrandan çıkmışmı kontrolü yapacağız
            # ekrandan çıkan mermiler mermi listesinden silinmeli, aksi taktirde binlerce mermi sonsuzluğa kadar gider bu da boşa kaynak sarfıdır.
            if not screen.get_rect().contains(bullet.rectangle):
                self.bullets.remove(
                    bullet)  # foreach döngülerinde bunu yapmak iyi bir yöntem değildir, çünkü dizin bozulur. Bir çok programlama dilinde hata alırsınız.
                # ancak burada python kabul etti :D
    def decrease(self,screen):
        self.bulletNumber -= 1

    def fire(self,screen,mposition):
        #Mermi sayisi 0 dan büyükse ateş etme işlemini gerçekleştiriyor
        if self.bulletNumber > 0:
            nbullet=Bullet(self,mposition)
            self.bullets.append(nbullet)
            self.decrease(screen)
            #her ateş edilişinde bir ateş edilme animasyonu devreye girmelidir
            #bu işlem farklı yollarla yapılabilir
            # burada yaprığımız normalde -1 olan shoot değerini 0  yapıyoruz ve nesnenin çizim fonksiyonunda bir if yapısıyla bu durumu kontrol ediyoruz.
            self.shootImageOrder=0
            #Her ateş ettiğinde mermi sayısı 1 azalıyor


    def expose(self):
        self.exposed=True



