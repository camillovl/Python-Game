from turtle import width
import pygame
from sys import exit
import random
from random import randint,choice


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        #Walking
        player_surface1 = pygame.image.load('WalkSoldier\Soldado (1).png').convert_alpha()
        player_surface2 = pygame.image.load('WalkSoldier\Soldado (2).png').convert_alpha()
        player_surface3 = pygame.image.load('WalkSoldier\Soldado (3).png').convert_alpha()
        player_surface4 = pygame.image.load('WalkSoldier\Soldado (4).png').convert_alpha()

        self.player_walk = [player_surface1,player_surface2,player_surface3,player_surface4]
        self.player_index = 0
        #self.player_surface = player_walk[player_index]

        self.image = self.player_walk[self.player_index]
        self.rect = self.image.get_rect(bottomright = (200,550))
        self.gravity = 0

        #Jumping
        player_jump1 = pygame.image.load('jumpSoldier\Tile050.png').convert_alpha
        player_jump2 = pygame.image.load('jumpSoldier\Tile051.png').convert_alpha
        player_jump3 = pygame.image.load('jumpSoldier\Tile052.png').convert_alpha
        player_jump4 = pygame.image.load('jumpSoldier\Tile053.png').convert_alpha

        self.player_jump = [player_jump1,player_jump2,player_jump3,player_jump4]
        self.player_index_jump = 0
        #self.player_surface_jump = player_jump[player_index_jump]
        
        self.image_jump = self.player_jump[self.player_index_jump]

        self.jump_sound = pygame.mixer.Sound('Jump.wav')
        self.jump_sound.set_volume(0.5)
    
    
    def player_animation(self):

        if self.rect.bottom < 550:
            self.player_index_jump += 0.1
        if self.player_index_jump >= len(self.player_jump):
            self.player_index_jump = 0
            self.player_image_jump = self.player_jump[int(self.player_index_jump)]

        else:
            self.player_index += 0.1
            if self.player_index >= len(self.player_walk):
                self.player_index = 0
            self.image = self.player_walk[int(self.player_index)]

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 550:
            self.gravity = -17
            self.jump_sound.play()


    
    def apply_gravity(self):
        self.gravity +=1
        self.rect.y += self.gravity
        if self.rect.bottom >= 550:
            self.rect.bottom = 550
    

    def update(self):
        self.player_input()
        self.apply_gravity()
        self.player_animation()

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

    def update(self):
        self.animation_state
        self.rect.x -= 6
        self.destroy()

    def destroy(self):
        if self.rect.x <= -100:
            self.kill()

#creating a timer
def display_timer():

    current_time = int(pygame.time.get_ticks() /100) - start_time
    timer_surface = test_font.render(f'{current_time}',False,(64,64,64)) #curren_time NEED TO BE AN INT
    timer_rect = timer_surface.get_rect(topleft = (425,50))
    screen.blit(timer_surface,timer_rect)
    #print(current_time)

def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 5

            if obstacle_rect.bottom == 550:
                screen.blit(snake_frames[snake_index], obstacle_rect)
                
            else:                
                #pygame.draw.rect(screen,'Blue',obstacle_rect)
                # screen.blit(stirge_surface,obstacle_rect)               
                screen.blit(stirge_frames[stirge_index], obstacle_rect)               
                
        
        
        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x >- 100] #this piece of code deletes the snakes that go out of screen
        # for obstacle in obstacle_list:
        #     if obstacle.x >- 100:
        #         aux.append(obstacle)

        return obstacle_list
    else:
         return []


    if obstacle_list:
        for obstacle_rect in obstacle_list:
            if player_rect.x >= obstacle_rect:
                score_value += 1


def collision_sprite(): 
    if pygame.sprite.spritecollide(player.sprite,obstacle_group,False):#1sprite, 2group, boolean:checks if the sprite collides with the group will be destroyed or noit
    #this entire statment returns a list if doesnt collide with anything is gonna return an empity list
        obstacle_group.empty()
        return False
    else:
        return True
        
#initializing pygame
pygame.init()

#Creating your screen and important variables
width = 800
height = 600
screen = pygame.display.set_mode((width,height)) #widht,height #(()) its a tuple
pygame.display.set_caption('MapleStory Wannabe') #setting the name of the game
clock = pygame.time.Clock()
test_font = pygame.font.Font('Pixeltype.ttf',30) #font type and font size
game_active = False
start_time = 0
bg_music = pygame.mixer.Sound('backgroudmusic.wav')
bg_music.set_volume(0.2)
bg_music.play(loops = -1) #plays the sound 4ever


#GROUPS
player = pygame.sprite.GroupSingle() #this is a group single
player.add(Player()) #this is a sprite

obstacle_group = pygame.sprite.Group()


background_surface = pygame.image.load('Backgrounds.png').convert_alpha() #converting an image to alpha facilitates pygame to read the code and make it lighter
background_surface = pygame.transform.scale(background_surface,(800,600))
title0_surface = pygame.image.load('Tiles\Dois.png').convert_alpha()
title1_surface = pygame.image.load('Tiles\Dois.png').convert_alpha()
title2_surface = pygame.image.load('Tiles\Dois.png').convert_alpha()
title3_surface = pygame.image.load('Tiles\Dois.png').convert_alpha()
title4_surface = pygame.image.load('Tiles\Dois.png').convert_alpha()

title5_surface = pygame.image.load('Tiles\Dois.png').convert_alpha()
title6_surface = pygame.image.load('Tiles\Dois.png').convert_alpha()
title7_surface = pygame.image.load('Tiles\Dois.png').convert_alpha()
title8_surface = pygame.image.load('Tiles\Dois.png').convert_alpha()

game_over = pygame.image.load('gameover.png').convert_alpha()

#score
score_surface = test_font.render('Score: ',False, 'Black')
score_rect = score_surface.get_rect(topleft = (600 ,40))

#timer
timer_surface = test_font.render('Timer: ', False, 'Black') #text you want to display, anti anliasing(False or True) , color
timer_rect = timer_surface.get_rect(topleft = (320,47 ))

#obstacles
snake_frame1 = pygame.image.load('Snake\Cobra 1.png').convert_alpha()
snake_frame1 = pygame.transform.scale(snake_frame1,(40,40))

snake_frame2 = pygame.image.load('Snake\Cobra 2.png').convert_alpha()
snake_frame2 = pygame.transform.scale(snake_frame2,(40,40))

snake_frame3 = pygame.image.load('Snake\Cobra 3.png').convert_alpha()
snake_frame3 = pygame.transform.scale(snake_frame3,(40,40))

snake_frame4 = pygame.image.load('Snake\Cobra 4.png').convert_alpha()
snake_frame4 = pygame.transform.scale(snake_frame4,(40,40))

snake_index = 0
snake_frames = [snake_frame1, snake_frame2, snake_frame3, snake_frame4]

snake_surface = snake_frames[snake_index]
#snake_surface = pygame.transform.scale(snake_surface,(30,25))
#snake_rect = snake_surface.get_rect(bottomright = (600,605))

#Stirge
stirge_frame1 = pygame.image.load('1.png').convert_alpha()
stirge_frame1 = pygame.transform.scale(stirge_frame1,(50,50))
stirge_frame2 = pygame.image.load('2.png').convert_alpha()
stirge_frame2 = pygame.transform.scale(stirge_frame2,(50,50))
stirge_index = 0
stirge_frames = [stirge_frame1, stirge_frame2]

stirge_surface = stirge_frames[stirge_index]

#stirge_frames[stirge_index] = pygame.transform.scale(stirge_surface,(30,25))


obstacle_rect_list = []

#Player

#Walking
player_surface1 = pygame.image.load('WalkSoldier\Soldado (1).png').convert_alpha()
player_surface2 = pygame.image.load('WalkSoldier\Soldado (2).png').convert_alpha()
player_surface3 = pygame.image.load('WalkSoldier\Soldado (3).png').convert_alpha()
player_surface4 = pygame.image.load('WalkSoldier\Soldado (4).png').convert_alpha()
player_walk = [player_surface1,player_surface2,player_surface3,player_surface4]
player_index = 0

player_surface = player_walk[player_index]

#Jumping
player_jump1 = pygame.image.load('jumpSoldier\Tile050.png').convert_alpha
player_jump2 = pygame.image.load('jumpSoldier\Tile051.png').convert_alpha
player_jump3 = pygame.image.load('jumpSoldier\Tile052.png').convert_alpha
player_jump4 = pygame.image.load('jumpSoldier\Tile053.png').convert_alpha
player_jump = [player_jump1,player_jump2,player_jump3,player_jump4]
player_index_jump = 0

player_surface_jump = player_jump[player_index_jump]

#Player RECTANGLE
player_rect = player_surface.get_rect(bottomright = (200,550)) #get the player surface and draws an rectangle around

#Gravity
player_gravity = 0

#intro screen
player_stand = pygame.image.load('WalkKing\Stand.png').convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand,0,3)
#player_stand =pygame.transform.scale(player_stand,(200,150))
player_stand_rect = player_stand.get_rect(center = (400,325))

#intro texts
intro_text = test_font.render('Press Enter to start the game', False, 'Black')
intro_rect = intro_text.get_rect(center = (420,200))

#Timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer,1400) # a timer ta trigger something every 900 miliseconds

snake_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(snake_animation_timer,100)

stirge_animation_timer = pygame.USEREVENT + 3
pygame.time.set_timer(stirge_animation_timer,200)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit() 

#inputs

        if game_active == True:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >= 550:
                    player_gravity = -17
            
            # code to clik on the player to jump if necessary

            #if event.type == pygame.MOUSEBUTTONDOWN:
                #if player_rect.collidepoint(event.pos):
                    #player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    game_active = True
                    #snake_rect.left = 800
                    start_time = int(pygame.time.get_ticks() /100)

        if game_active == True:
            if event.type == obstacle_timer:
                obstacle_group.add(Obstacle(choice(['stirge','snail','snail'])))
    
            if event.type == snake_animation_timer and game_active == True:
                snake_index = (snake_index + 1) % 4
             
            if event.type == stirge_animation_timer and game_active == True:
                stirge_index = (stirge_index + 1) % 2

                
    if game_active == True:
    #background

        screen.blit(background_surface,(0,0))
        #screen.fill((255,255,255))
        #screen.blit(background_surface,(0,0))
    #Ground
        screen.blit(title0_surface,(0,550))  #blit is used when you want to put a surface in another surface    
        screen.blit(title1_surface,(128,550))  #blit is used when you want to put a surface in another surface    
        screen.blit(title2_surface,(256,550))  #blit is used when you want to put a surface in another surface    
        screen.blit(title3_surface,(384,550))  #blit is used when you want to put a surface in another surface    
        screen.blit(title4_surface,(512,550))  #blit is used when you want to put a surface in another surface    
        screen.blit(title5_surface,(640,550))  #blit is used when you want to put a surface in another surface    
        screen.blit(title6_surface,(672,550))  #blit is used when you want to put a surface in another surface    
        screen.blit(title7_surface,(800,550))  #blit is used when you want to put a surface in another surface    
        screen.blit(title8_surface,(928,550))  #blit is used when you want to put a surface in another surface    
    
    #score

    #timer
        #pygame.draw.rect(screen,'Black',score_rect)
        screen.blit(timer_surface,timer_rect)
        display_timer()

    #Drawingand updating the player class
        player.draw(screen)
        player.update()

    #Drawing and updating the Obstacle class
        obstacle_group.draw(screen)
        obstacle_group.update()

    #Colision 
        game_active = collision_sprite()
        #simulating the colision with the floor
        if player_rect.bottom >= 550:
            player_rect.bottom = 550
        

    if game_active == False:
        screen.fill((200,200,200))#the numbers mean colors
        screen.blit(player_stand,player_stand_rect)
        screen.blit(intro_text,intro_rect)
        obstacle_rect_list.clear() #debug the colision to restart the game properly
       
        #these two following lines makes the character get back to the proper position when restarting the game
        player_rect.midbottom = (80,550)
        player_gravity = 0

    #update 
    # everything
    pygame.display.update() #updating the display surface above
    clock.tick(60) #this '60' tells-me that my the while true loop shouldnt not run faster than 60fps
