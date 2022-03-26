import constant as cs 
class PlayerInfo:
    def __init__(self):
        self.score=cs.SCORE
        self.life=cs.LIFE
        self.level=cs.LEVEL

    def set_score(self):
        self.score+=1

    def get_score(self):
        return self.score

    def set_life(self):
            self.life-=1
        
    def get_life(self):
        return self.life
    
    def set_level(self):
            self.level+=1
        
    def get_level(self):
        return self.level
    
    def reset_info(self):
        self.score=0
        self.life=5
        self.level=0