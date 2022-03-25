from class_theship import MyShip
from class_bullet import Bullet
import os 
import pygame 
import constant as cs 


class Player(MyShip):
    def __init__(self, x, y):
        super().__init__(x,y)
        self.load_img()
        self.mask=pygame.mask.from_surface(self.ship_img)

    def load_img(self):
        self.SHIP_PATH = os.path.join(os.getcwd(),"images/ship.png")
        self.ship_img = pygame.transform.scale(pygame.image.load(self.SHIP_PATH),cs.IMAGE_SIZE)
    
    def shoot_delay(self):
        if self.counter_cool_down >= cs.COOLDOWN:
            self.counter_cool_down =0;
        elif self.counter_cool_down > 0:
            self.counter_cool_down+=1

    def move_bullet(self):
        self.shoot_delay()
        for bullet in self.bul:
            bullet.move(cs.BULLET_SPEED)
            if bullet.off_frame():
                self.bul.remove(bullet)

    def shoot(self):
        if self.counter_cool_down==0:
            self.bullet = Bullet(self.position_x()+20, self.position_y()+10)
            self.bul.append(self.bullet) 
            self.counter_cool_down=1

    def collide(self, ob2):
        off_x = ob2.position_x() - self.position_x()
        off_y = ob2.position_y() - self.position_y()
        return self.mask.overlap(ob2.mask,(off_x,off_y)) !=None

    def move_center(self):
        self.x = cs.WIDTH/2
        self.y = cs.HEIGHT-100
        
    def move_shoot(self, keys):
        if keys[pygame.K_LEFT] and self.position_x()-cs.PLAYER_SPEED > 0:
            self.move_left(cs.PLAYER_SPEED)
        if keys[pygame.K_RIGHT] and self.position_x()+cs.PLAYER_SPEED + self.get_img_width()< cs.WIDTH:
            self.move_right(cs.PLAYER_SPEED)
        if keys[pygame.K_UP] and self.position_y()-cs.PLAYER_SPEED > 0:
            self.move_up(cs.PLAYER_SPEED)
        if keys[pygame.K_DOWN] and self.position_y()+cs.PLAYER_SPEED + self.get_img_height()< cs.HEIGHT:
            self.move_down(cs.PLAYER_SPEED)
        if keys[pygame.K_SPACE]:
            self.shoot()

