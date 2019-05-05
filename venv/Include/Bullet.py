import pygame
from pygame.math import Vector2
import sys
import math
import random

class Bullet():
    def __init__(self,plane,mposition):
        self.x = plane.x
        self.y = plane.y
        self.mx = 0 #x haraket yönü
        self.my = 0 #x haraket yönü
        self.mposition = mposition

        self.rectangle=pygame.rect.Rect(plane.rectangle.center[0], plane.rectangle.center[1], int(plane.rectangle[2] / 5), int(plane.rectangle[3] / 5))
        self.imageOrder=0
        self.images=[pygame.transform.scale(pygame.image.load("images/png/Bullet/Bullet (1).png"),(self.rectangle[2],self.rectangle[3])),pygame.transform.scale(pygame.image.load("images/png/Bullet/Bullet (2).png"),(self.rectangle[2],self.rectangle[3])),pygame.transform.scale(pygame.image.load("images/png/Bullet/Bullet (3).png"),(self.rectangle[2],self.rectangle[3])),pygame.transform.scale(pygame.image.load("images/png/Bullet/Bullet (4).png"),(self.rectangle[2],self.rectangle[3])),pygame.transform.scale(pygame.image.load("images/png/Bullet/Bullet (5).png"),(self.rectangle[2],self.rectangle[3]))]
    def draw(self,screen):
        self.imageOrder=(self.imageOrder+1)%5
        bullet_vec_x = self.mposition[0] - self.x
        bullet_vec_y = self.mposition[1] - self.y
        vec_length = math.sqrt(bullet_vec_x ** 2 + bullet_vec_y ** 2)
        bullet_vec_x = (bullet_vec_x / vec_length) * 2
        bullet_vec_y = (bullet_vec_y / vec_length) * 2
        self.mx += bullet_vec_x
        self.my += bullet_vec_y
        self.rectangle[0]=self.rectangle[0] + self.mx
        self.rectangle[1]=self.rectangle[1] + self.my



        screen.blit(self.images[self.imageOrder], self.rectangle)
