import pygame

class Goal(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((32, 32))
        self.image.fill("green")
        self.rect = self.image.get_rect(topleft = pos)
        
        #player movement
        self.direction = pygame.math.Vector2(0,0)

    # def update(self):
    #     self.rect.x += self.direction.x * 3
    #     self.rect.y += self.direction.y * 3

        