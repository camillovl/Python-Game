import pygame
from random import choice

class Obstacle(pygame.sprite.Sprite):
    def __init__(self,type,screen):
        self.type = type
        self.screen = screen

        super().__init__()
        self.obstacle_index = 0
        self.frames = []
        
        
        if self.type == 'stirge':
            stirge_frame1 = pygame.image.load('1.png').convert_alpha()
            stirge_frame1 = pygame.transform.scale(stirge_frame1,(50,50))
            stirge_frame2 = pygame.image.load('2.png').convert_alpha()      
            stirge_frame2 = pygame.transform.scale(stirge_frame2,(50,50))
            
            self.frames = [stirge_frame1, stirge_frame2]
            #self.stirge_index = 0
            #self.stirge_surface = stirge_frames[stirge_index]

            self.image = self.frames[0]
            self.rect = self.image.get_rect(bottomright = (700,515))

        else:
            snake_frame1 = pygame.image.load('Snake\Cobra 1.png').convert_alpha()
            snake_frame1 = pygame.transform.scale(snake_frame1,(40,40))

            snake_frame2 = pygame.image.load('Snake\Cobra 2.png').convert_alpha()
            snake_frame2 = pygame.transform.scale(snake_frame2,(40,40))

            snake_frame3 = pygame.image.load('Snake\Cobra 3.png').convert_alpha()
            snake_frame3 = pygame.transform.scale(snake_frame3,(40,40))

            snake_frame4 = pygame.image.load('Snake\Cobra 4.png').convert_alpha()
            snake_frame4 = pygame.transform.scale(snake_frame4,(40,40))

           
            self.frames = [snake_frame1, snake_frame2, snake_frame3, snake_frame4]
            #self.snake_index = 0
            #snake_surface = snake_frames[snake_index]

            self.image = self.frames[0]
            self.rect = self.image.get_rect(bottomright = (700,550))
        
        #self.obstacle_index    
      
    def obstacle_animation(self):
        #if type == 'stirge':
        self.obstacle_index += 0.1
        if self.obstacle_index >= len(self.frames):
            self.obstacle_index = 0
        self.image = self.frames[int(self.obstacle_index)]



    # def obstacle_movement(self):
        
    #     obstacle1
    #     obstacle2 = pygame.draw.rect(screen,)

    # def obstacle_movement(self):
    #     if obstacle_list:
    #         for obstacle_rect in obstacle_list:
    #             obstacle_rect.x -= 5

    #         if self.type == 'stirge':
    #             self.screen.blit(self.frames[self.obstacle_index], obstacle_rect)
                
    #         else:                
    #             #pygame.draw.rect(screen,'Blue',obstacle_rect)
    #             # screen.blit(stirge_surface,obstacle_rect)               
    #             self.screen.blit(self.frames[self.obstacle_index], obstacle_rect)               
                
        
        
    #         obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x >- 100] #this piece of code deletes the snakes that go out of screen
    #         # for obstacle in obstacle_list:
    #         #     if obstacle.x >- 100:
    #         #         aux.append(obstacle)

    #         return obstacle_list
    #     else:
    #         return []

    def update(self):
        #(choice(['stirge','snake','snake'])))
        #choice(['stirge', 'snake', 'snake'])
        self.obstacle_animation()
        #self.rect.x -= 6
        self.destroy()
    
    def checkNewObstacle(self):
        self = Obstacle(choice(['stirge', 'snake', 'snake']))

    def destroy(self):
        if self.rect.x <= -100:
            self.kill()
