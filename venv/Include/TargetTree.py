import pygame
import sys
import math
import random
import ScoreBoard

class TargetTree():

    ExposedEvent=pygame.event.Event(pygame.USEREVENT, attr1='TargetTreeExposed')
    def __init__(self, screen):

        self.life = 100
        width = screen.get_width()
        height = screen.get_height()
        ##Targerlerin Random olarak bir taraftan gelmesi için
        side = random.randint(1, 4)
        if side == 1:
            self.x = random.randint(0, width)
            self.y = height
        elif side == 2:
            self.x = random.randint(0, width)
            self.y = 0
        elif side == 3:
            self.x = width
            self.y = random.randint(0, height)
        elif side == 4:
            self.x = 0
            self.y = random.randint(0, height)
        ##Targetlerin gemiye doğru hareket etmesi için
        bullet_vec_x = width/2 - self.x
        bullet_vec_y = height/2 - self.y
        vec_length = math.sqrt(bullet_vec_x ** 2 + bullet_vec_y ** 2)
        bullet_vec_x = (bullet_vec_x / vec_length) * 2
        bullet_vec_y = (bullet_vec_y / vec_length) * 2
        self.mx = bullet_vec_x
        self.my = bullet_vec_y
        self.rectangle=pygame.rect.Rect(self.x+int(width/20)/2,self.y+int(height/10)/2,int(width/20),int(height/10))

        self.flyImageOrder = 0
        self.flyImages = []
        for i in range(1, 10):
            self.flyImages.append(
                pygame.transform.scale(pygame.image.load("images/png/Bombs/Bomb_3_Idle_00" + str(i) + ".png"),
                                       (self.rectangle[2], self.rectangle[3])))

        self.explosionImageOrder = -1
        self.explosionImages = []
        for i in range(1, 9):
            self.explosionImages.append(
                pygame.transform.scale(pygame.image.load("images/png/Bombs/Bomb_3_Explosion_00" + str(i) + ".png"),
                                       (self.rectangle[2] * 4, self.rectangle[2] * 4)))
        self.exposed = False

    def draw(self, screen):
        if self.explosionImageOrder == -1:
            self.flyImageOrder = (self.flyImageOrder + 1) % 8
            self.rectangle.centerx = self.rectangle.centerx + self.mx
            self.rectangle.centery = self.rectangle.centery + self.my
            screen.blit(self.flyImages[self.flyImageOrder],
                        [self.rectangle[0] - int(self.flyImages[self.flyImageOrder].get_height() / 2),
                         self.rectangle[1] - int(self.flyImages[self.flyImageOrder].get_width() / 2)])
        else:
            self.explosionImageOrder = (self.explosionImageOrder + 1) % 9
            if self.explosionImageOrder == 8:
                return True
            screen.blit(self.explosionImages[self.explosionImageOrder],
                        [self.rectangle[0] - int(self.explosionImages[self.explosionImageOrder].get_width() / 2),
                         self.rectangle[1] - int(self.explosionImages[self.explosionImageOrder].get_height() / 2)])
        return False

    def hit(self,plane):
        #5 Vuruşta Öleceği için 2. Targetin canı 100. 20 azaltıyoruz
        self.life = self.life - 20
        if self.life <= 0:
            #Eğer Targetimiz ölürse Plane 10 adet cephane ekliyoruz
            plane.bulletNumber += 10
            ScoreBoard.ScoreBoard.set_Score(10)
            self.expose()

    def expose(self):
        self.life = 0

        self.exposed = True
        if self.explosionImageOrder < 0:
            self.explosionImageOrder = 0
