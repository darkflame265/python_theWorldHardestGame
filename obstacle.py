import pygame

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((32, 32))
        self.image.fill("blue")
        self.rect = self.image.get_rect(topleft = pos)
        
        
        #player movement
        self.direction = pygame.math.Vector2(0,0)
        self.speed = 3
        self.t0 = 0
        self.num = 0
        self.count = 0
            
    def move(self):
        if (self.direction.x >= 0):
            self.direction.x = -1.0
        elif ( self.direction.x < 0):
            self.direction.x = 1.0
            
    def set_move_course_r_to_l(self):
        start_ticks = pygame.time.get_ticks()
        if (start_ticks - self.t0 > 1000):
            if (self.direction.x >= 0):
                self.direction.x = -1.0
            elif ( self.direction.x < 0):
                self.direction.x = 1.0
            self.t0 = start_ticks
            
    def set_move_course_down_to_up(self):
        start_ticks = pygame.time.get_ticks()
        if (start_ticks - self.t0 > 1000):
            if (self.direction.y >= 0):
                self.direction.y = -1.0
            elif ( self.direction.y < 0):
                self.direction.y = 1.0
            self.t0 = start_ticks
            
    
    def set_move_course_roll(self):
        start_ticks = pygame.time.get_ticks()
        if (start_ticks - self.t0 > 10):
            if (self.count == 0):
                self.direction.x = 1.0
                self.direction.y = 0
                self.count += 1
            elif (self.count == 1):
                self.direction.x = 0
                self.direction.y = 1.0
                self.count += 1
            elif (self.count == 2):
                self.direction.x = -1.0
                self.direction.y = 0
                self.count += 1
            elif (self.count == 3):
                self.direction.x = 0
                self.direction.y = -1.0
                self.count = 0
            self.t0 = start_ticks
            self.speed = 9
            
    def set_move_course_up_to_down(self):
        start_ticks = pygame.time.get_ticks()
        if (start_ticks - self.t0 > 1000):
            if (self.direction.y <= 0):
                self.direction.y = 1.0
            elif ( self.direction.y > 0):
                self.direction.y = -1.0
            self.t0 = start_ticks
            
    def set_move_course_l_to_r(self):
        start_ticks = pygame.time.get_ticks()
        if (start_ticks - self.t0 > 1000):
            if (self.direction.x <= 0):
                self.direction.x = 1.0
            elif ( self.direction.x > 0):
                self.direction.x = -1.0
            self.t0 = start_ticks
        
    def update(self):
        if (self.num == 0):
            self.set_move_course_r_to_l()
        elif(self.num == 1):
            self.set_move_course_down_to_up()
        elif(self.num == 2):
            self.set_move_course_roll()
        elif(self.num == 3):
            self.set_move_course_up_to_down()
        elif(self.num == 4):
            self.set_move_course_l_to_r()
            
        self.rect.x += self.direction.x * self.speed
        self.rect.y += self.direction.y * self.speed

        