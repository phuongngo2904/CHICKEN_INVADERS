import os
import pygame
import constant as cs

class Bullet:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.load_img()
        self.mask = pygame.mask.from_surface(self.bullet_img)

    def off_frame(self):
        return self.position_y() <=0

    def move(self,speed):
        self.y -= speed

    def position_x(self):
        return self.x

    def position_y(self):
        return self.y

    def get_img_width(self):
        return self.ship_img.get_width()

    def get_img_height(self):
        return self.ship_img.get_height()

    def load_img(self):
        self.BULLET_PATH = os.path.join(os.getcwd(),"images/bullet.png")
        self.bullet_img = pygame.transform.scale(pygame.image.load(self.BULLET_PATH),cs.BULLET_SIZE)

    def draw(self,window):
        window.blit(self.bullet_img,(self.x, self.y))
