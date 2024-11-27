import pygame
from tiles import Tile
from Settings import *
from player import Player
from obstacle import Obstacle
from goal_sprite import Goal
from functools import partial

class Level:
    def __init__(self, levelData, surface):
        self.displaySurface = surface
        self.setupLevel(levelData)
        self.world_shift = 0
    

    def setupLevel(self, layout):
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.obstacle = pygame.sprite.Group()
        self.goal = pygame.sprite.Group()
        
        for rowIndex, row in enumerate(layout):
            for colIndex, cell in enumerate(row):
                x = colIndex * tile_size
                y = rowIndex * tile_size
                
                if cell == 'X':
                    tile = Tile((x,y), tile_size)
                    self.tiles.add(tile)
                if cell == 'P':
                    player_sprite = Player((x, y))
                    self.player.add(player_sprite)
                    self.x = x
                    self.y = y
                if cell == 'G':
                    goal_sprite = Goal((x, y))
                    self.goal.add(goal_sprite)
                if cell == 'L':
                    obstacle_sprite = Obstacle((x, y))
                    self.obstacle.add(obstacle_sprite)
                if cell == 'U':
                    obstacle_sprite = Obstacle((x, y))
                    self.obstacle.add(obstacle_sprite)
                    obstacle_sprite.num = 1
                if cell == '2':
                    obstacle_sprite = Obstacle((x, y))
                    self.obstacle.add(obstacle_sprite)
                    obstacle_sprite.num = 2
                if cell == 'D':
                    obstacle_sprite = Obstacle((x, y))
                    self.obstacle.add(obstacle_sprite)
                    obstacle_sprite.num = 3
                if cell == 'R':
                    obstacle_sprite = Obstacle((x, y))
                    self.obstacle.add(obstacle_sprite)
                    obstacle_sprite.num = 4
                    
    def detect_collision(self):
        player = self.player.sprite
        obstacle = self.obstacle.sprites
        goal = self.goal.sprites
        
        #플레이어와 타일이 충돌시.
        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                player.rect.x = self.x
                player.rect.y = self.y
                
        #obsctacle과 플레이어 충돌시
        for sprite in self.obstacle.sprites():
            if sprite.rect.colliderect(player.rect):
                #player.image.fill("blue")
                player.rect.x = self.x
                player.rect.y = self.y
                
        #goal과 플레이어 충돌시
        for sprite in self.goal.sprites():
            if sprite.rect.colliderect(player.rect):
                sprite.image.fill("purple")
                self.x = sprite.rect.x
                self.y = sprite.rect.y
                
    def run(self):
        self.tiles.update(self.world_shift)
        self.player.update()
        self.obstacle.update()

        self.detect_collision()
    
        #화면에 그리기
        self.tiles.draw(self.displaySurface)
        self.player.draw(self.displaySurface)
        self.obstacle.draw(self.displaySurface)
        self.goal.draw(self.displaySurface)
        
        