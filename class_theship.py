class MyObj:
    def __init__(self, x, y):
        self.x=x
        self.y=y
        self.ship_img=None
        self.bul=[]
        self.counter_cool_down=0

    def draw(self,window):
        window.blit(self.ship_img,(self.x, self.y))
        for bullet in self.bul:
            bullet.draw(window)

    def move_left(self, player_speed):
        self.x -= player_speed

    def move_right(self, player_speed):
        self.x += player_speed

    def move_up(self, player_speed):
        self.y -= player_speed

    def move_down(self, player_speed):
        self.y += player_speed

    def position_x(self):
        return self.x

    def position_y(self):
        return self.y

    def get_img_width(self):
        return self.ship_img.get_width()

    def get_img_height(self):
        return self.ship_img.get_height()
