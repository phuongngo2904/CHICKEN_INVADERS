import os
from pickle import FALSE
import random
import pygame
import constant as cs
from class_theplayer import Player
from class_theenemy import Enemy

class MyGame:
    def __init__(self):
        pygame.font.init()
        self.MAIN_FONT = pygame.font.SysFont(cs.FONT, cs.F_SIZE)
        self.WINDOW = pygame.display.set_mode((cs.WIDTH, cs.HEIGHT))
        self.load_background_img()

    def load_background_img(self):
        self.BG_PATH = os.path.join(os.getcwd(),"images/backgorund.png")
        self.BG = pygame.transform.scale(pygame.image.load(self.BG_PATH),(cs.WIDTH,cs.HEIGHT))

    def redraw_window(self):
        self.WINDOW.blit(self.BG,(0,0))
        self.score_label = self.MAIN_FONT.render(f"SCORE: {cs.SCORE}",1,(0, 204, 0))
        self.life_label = self.MAIN_FONT.render(f"LIFE: {cs.LIFE}",1,(0, 204, 0))
        self.level_label = self.MAIN_FONT.render(f"LEVEL: {cs.LEVEL}",1,(0, 204, 0))

        self.WINDOW.blit(self.score_label,(10,10))
        self.WINDOW.blit(self.level_label,(300,10))
        self.WINDOW.blit(self.life_label,(cs.WIDTH - self.life_label.get_width()-10, 10))

        if cs.GAME_OVER:
            self.go_label = self.MAIN_FONT.render(f"GAME OVER ! Your score is {cs.SCORE}",1,(255,255,255))
            self.WINDOW.blit(self.go_label,(cs.WIDTH/2-self.go_label.get_width()/2,cs.HEIGHT/2))

        for e in cs.ENEMY:
            e.draw(self.WINDOW)
        self.player.draw(self.WINDOW)
        pygame.display.update()

    def set_up(self):
        self.clock=pygame.time.Clock()
        self.player = Player(cs.WIDTH/2,cs.HEIGHT-100)
        pygame.display.set_caption("CHICKEN INVADERS")

    def lose_a_life(self):
        while cs.LOST:  
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key==pygame.K_SPACE:
                        cs.LOST=False
        pygame.display.set_mode((cs.WIDTH, cs.HEIGHT))
        self.player.move_center()
        pygame.display.update() 

    def run_game(self):
        while cs.RUN:
            self.clock.tick(cs.FPS)
            self.redraw_window()

            if cs.LIFE==0:
                cs.GAME_OVER=True
                cs.GO_COUNTER+=1

            if cs.GAME_OVER:
                if cs.GO_COUNTER > cs.FPS*4:
                    cs.RUN=False
                else:
                    continue

            if cs.LOST and not cs.GAME_OVER:
                self.lose_a_life()

            if cs.LEVEL == 5:
                cs.ENEMY_SPEED+=1

            if len(cs.ENEMY)==0:
                cs.WAVE+=2
                for i in range(cs.WAVE):
                    enemy = Enemy(random.randrange(0, cs.WIDTH-100),random.randrange(-1600,-100),random.choice(["1","2","3","4"]))
                    cs.ENEMY.append(enemy)
                    
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    cs.RUN=False
            keys = pygame.key.get_pressed()
            if(keys[pygame.K_ESCAPE]): #QUIT GAME
                cs.RUN=False
            self.player.move_shoot(keys)
            self.player.move_bullet()

            for e in cs.ENEMY[:]:
                e.move(cs.ENEMY_SPEED)
                if self.player.collide(e):
                    cs.LIFE-=1
                    cs.LOST = True
                if e.collide(self.player.bul):
                    e.get_hit()
                if e.position_y() + e.get_img_height() > cs.HEIGHT:
                    cs.ENEMY.remove(e)
                if e.current_hit()==0:
                    cs.SCORE+=1
                    if cs.SCORE==cs.PREVIOUS_SCORE+10:
                        cs.LEVEL +=1
                        cs.PREVIOUS_SCORE=cs.SCORE
                    cs.ENEMY.remove(e)
        pygame.quit()

