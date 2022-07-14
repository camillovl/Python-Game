import pygame
from random import randint
import random


class Obstacle(pygame.sprite.Sprite):
    def __init__(self,type):
        super().__init__()

        if type == 'stirge':
            stirge_frame1 = pygame.image.load('1.png').convert_alpha()
            stirge_frame1 = pygame.transform.scale(stirge_frame1,(50,50))
            stirge_frame2 = pygame.image.load('2.png').convert_alpha()      
            stirge_frame2 = pygame.transform.scale(stirge_frame2,(50,50))

            #stirge_index = 0
            self.frames = [stirge_frame1, stirge_frame2]
            #stirge_surface = stirge_frames[stirge_index]
            y_pos = 515
        else:
            snake_frame1 = pygame.image.load('Snake\Cobra 1.png').convert_alpha()
            snake_frame1 = pygame.transform.scale(snake_frame1,(40,40))

            snake_frame2 = pygame.image.load('Snake\Cobra 2.png').convert_alpha()
            snake_frame2 = pygame.transform.scale(snake_frame2,(40,40))

            snake_frame3 = pygame.image.load('Snake\Cobra 3.png').convert_alpha()
            snake_frame3 = pygame.transform.scale(snake_frame3,(40,40))

            snake_frame4 = pygame.image.load('Snake\Cobra 4.png').convert_alpha()
            snake_frame4 = pygame.transform.scale(snake_frame4,(40,40))

            #snake_index = 0
            self.frames = [snake_frame1, snake_frame2, snake_frame3, snake_frame4]
            #snake_surface = snake_frames[snake_index]
            y_pos = 550

        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom = (random.randint(900,1100),y_pos))
    
    def animation_state(self):
        self.animation_index += 0.1
        if self.animation_index >=len(self.frames):
            self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]


    def destroy(self):
        if self.rect.x <= -100:
            self.kill()
    
    def update(self):
        self.animation_state
        self.rect.x -= 6
        self.destroy()