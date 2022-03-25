from Game import MyGame
import os
import random
import pygame
import constant as cs

if __name__ == "__main__":
    pygame.font.init()
    MAIN_FONT = pygame.font.SysFont(cs.FONT, cs.F_SIZE)
    WINDOW = pygame.display.set_mode((cs.WIDTH, cs.HEIGHT))
    BG_PATH = os.path.join(os.getcwd(),"images/backgorund.png")
    BG = pygame.transform.scale(pygame.image.load(BG_PATH),(cs.WIDTH,cs.HEIGHT))
    run = True
    while run:
        welcome_label = MAIN_FONT.render(f"---Welcome to Chicken Invaders---",1,(255,255,255))
        WINDOW.blit(BG,(0,0))
        WINDOW.blit(welcome_label,((cs.WIDTH/2-welcome_label.get_width()/2),cs.HEIGHT/2))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    run=False
                    pygame.quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    newgame=MyGame()
                    newgame.set_up() 
                    newgame.run_game()
    
