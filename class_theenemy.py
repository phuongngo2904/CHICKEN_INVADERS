from class_theobj import MyObj
import os
import pygame
import constant as cs 

#LOAD CHICKENS
C1_PATH = os.path.join(os.getcwd(),"images/c1.png")
C1_IMG = pygame.transform.scale(pygame.image.load(C1_PATH),cs.IMAGE_SIZE)

C2_PATH = os.path.join(os.getcwd(),"images/c2.png")
C2_IMG = pygame.transform.scale(pygame.image.load(C2_PATH),cs.IMAGE_SIZE)

C3_PATH = os.path.join(os.getcwd(),"images/c3.png")
C3_IMG = pygame.transform.scale(pygame.image.load(C3_PATH),cs.IMAGE_SIZE)

C4_PATH = os.path.join(os.getcwd(),"images/c4.png")
C4_IMG = pygame.transform.scale(pygame.image.load(C4_PATH),cs.IMAGE_SIZE)

class Enemy(MyObj):
    TYPE = {"1": C1_IMG,
            "2": C2_IMG,
            "3": C3_IMG,
            "4": C4_IMG,
            }
    def __init__(self, x, y, type, hit=2):
        super().__init__(x,y)
        self.ship_img=self.TYPE[type]
        self.mask=pygame.mask.from_surface(self.ship_img)
        self.hit=hit
    
    def get_hit(self):
        self.hit-=1

    def current_hit(self):
        return self.hit
        
    def collide(self,bullet):
        for b in bullet:
            off_x = b.position_x() - self.position_x()
            off_y = b.position_y() - self.position_y()
            return self.mask.overlap(b.mask,(off_x,off_y)) !=None
            
    def move(self,speed):
        self.y+=speed;