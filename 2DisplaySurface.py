import pygame
from sys import exit
from random import randint

#creating a score mode
def display_score():
    current_time = int(pygame.time.get_ticks() /100) - start_time
    score_surface = test_font.render(f'{current_time}',False,(64,64,64)) #curren_time NEED TO BE AN INT
    score_rect = score_surface.get_rect(topleft = (425,50))
    screen.blit(score_surface,score_rect)
    print(current_time)

def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 4

            if obstacle_rect.bottom == 550:
                # pygame.draw.rect(screen,'Blue',obstacle_rect)
                # screen.blit(snake_surface,obstacle_rect)
                screen.blit(snake_frames[snake_index], obstacle_rect)
                
            else:                
                pygame.draw.rect(screen,'Blue',obstacle_rect)
                # screen.blit(stirge_surface,obstacle_rect)               
                screen.blit(stirge_frames[stirge_index], obstacle_rect)               
                
        
        
        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x >- 100] #this piece of code deletes the snakes that go out of screen
        # for obstacle in obstacle_list:
        #     if obstacle.x >- 100:
        #         aux.append(obstacle)

        return obstacle_list
    else: return []


def collisions(player,obstacles):

    if obstacles:
        for obstacles_rect in obstacles:
            if player.colliderect(obstacles_rect): return game_active == False
    return game_active == True


def player_animation():
    global player_surface, player_index, player_surface_jump, player_index_jump

    if player_rect.bottom < 550:
        player_index_jump += 0.1
        if player_index_jump >= len(player_jump):
            player_index_jump = 0
        player_surface_jump = player_jump[int(player_index_jump)]

    else:
        player_index += 0.1
        if player_index >= len(player_walk):
            player_index = 0
        player_surface = player_walk[int(player_index)]

   
#initializing pygame
pygame.init()

#Creating your screen and important variables
screen = pygame.display.set_mode((800,600)) #widht,height #(()) its a tuple
pygame.display.set_caption('MapleStory Wannabe') #setting the name of the game
clock = pygame.time.Clock()
test_font = pygame.font.Font('Pixeltype.ttf',30) #font type and font size
game_active = False
#start_time = 0

#background_surface = pygame.image.load('backgrounds.png').convert_alpha() #converting an image to alpha facilitates pygame to read the code and make it lighter

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
score_surface = test_font.render('Timer:', False, 'Black') #text you want to display, anti anliasing(False or True) , color
score_rect = score_surface.get_rect(topleft = (320,47 ))

#obstacles
snake_frame1 = pygame.image.load('Snake\Cobra 1.png').convert_alpha()
snake_frame2 = pygame.image.load('Snake\Cobra 2.png').convert_alpha()
snake_frame3 = pygame.image.load('Snake\Cobra 3.png').convert_alpha()
snake_frame4 = pygame.image.load('Snake\Cobra 4.png').convert_alpha()
snake_index = 0
snake_frames = [snake_frame1, snake_frame2, snake_frame3, snake_frame4]

snake_surface = snake_frames[snake_index]
#snake_surface = pygame.transform.scale(snake_surface,(30,25))
#snake_rect = snake_surface.get_rect(bottomright = (600,605))

#Stirge
stirge_frame1 = pygame.image.load('1.png').convert_alpha()
stirge_frame2 = pygame.image.load('2.png').convert_alpha()
stirge_index = 0
stirge_frames = [stirge_frame1, stirge_frame2]

stirge_surface = stirge_frames[stirge_index]

#stirge_surface = pygame.transform.scale(stirge_surface,(30,25))

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
player_stand_rect = player_stand.get_rect(center = (500,325))

#intro texts
intro_text = test_font.render('Press R to start the game', False, 'Black')
intro_rect = intro_text.get_rect(center = (500,200))

#Timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer,1400) # a timer ta trigger something every 900 miliseconds

snake_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(snake_animation_timer,1500)

stirge_animation_timer = pygame.USEREVENT + 3
pygame.time.set_timer(stirge_animation_timer,200)


#defining the color of the background (display surface)
#test_surface = pygame.Surface((100,200))
#test_surface.fill('Red')
 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit() 

#inputs

        if game_active == True:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >= 550:
                    player_gravity = -15
            
            # code to clik on the player to jump if necessary

            #if event.type == pygame.MOUSEBUTTONDOWN:
                #if player_rect.collidepoint(event.pos):
                    #player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    game_active = True
                    #snake_rect.left = 800
                    start_time = int(pygame.time.get_ticks() /100)

        if game_active == True:
            if event.type == obstacle_timer:
                if randint(0,2):#random statment that triggers true or false (0 or 1)
                    obstacle_rect_list.append(snake_frames[snake_index].get_rect(bottomright = (randint(1100,1200),550)))
                else:
                    obstacle_rect_list.append(stirge_frames[stirge_index].get_rect(bottomright = (randint(1100,1200),530)))
                    #print('test')
    
            if event.type == snake_animation_timer and game_active == True:
                snake_index = (snake_index + 1) % 4
             
            if event.type == stirge_animation_timer and game_active == True:
                stirge_index = (stirge_index + 1) % 2

        # if game_active == True:
        #     if event.type == obstacle_timer:
        #         if randint(0,2):#random statment that triggers true or false (0 or 1)
        #             obstacle_rect_list.append(snake_surface.get_rect(bottomright = (randint(1100,1200),550)))
        #         else:
        #             obstacle_rect_list.append(stirge_surface.get_rect(bottomright = (randint(1100,1200),530)))
        #             #print('test')
    
        #     if event.type == snake_animation_timer and game_active == True:
        #         if snake_index == 0:
        #             snake_index = 1

        #         if snake_index == 1:
        #             snake_index = 2

        #         if snake_index == 2:
        #             snake_index = 3

        #         else:
        #             snake_index = 0
        #         snake_surface = snake_frames[snake_index]

             
        #     if event.type == stirge_animation_timer and game_active == True:
        #         if stirge_index == 0:
        #             stirge_index = 1
        #         else:
        #             stirge_index = 0
        #             stirge_surface = stirge_frames[stirge_index]
                
    if game_active == True:
    #background
        screen.fill((255,255,255))
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
    #Score  
        #pygame.draw.rect(screen,'Black',score_rect)
        screen.blit(score_surface,score_rect)
        display_score()
        
    #Snake   
        # snake_rect.x -= 3
        # if snake_rect.right <= 0:
        #     snake_rect.left = 1000
        # #pygame.draw.rect(screen,'Red',snake_rect)
        # screen.blit(snake_surface,(snake_rect))

    #player
        player_gravity += 1
        player_rect.y += player_gravity
        
        #simulating the colision with the floor
        if player_rect.bottom >= 550:
            player_rect.bottom = 550

        player_animation()

        
        #pygame.draw.rect(screen,'Blue',player_rect)
        screen.blit(player_surface,(player_rect))   

    #Obstacle movement
        obstacle_rect_list = obstacle_movement(obstacle_rect_list)

    #collision

        game_active = collisions(player_rect,obstacle_rect_list) #collisions can return false or true, if the player hits an obstacle it will return false ending the

        #player_rect.colliderect(snake_rect)
        #print(player_rect.colliderect(snake_rect)) #the moment rectangle colides it becames true
        
        #End the game if the player touches the snake
        

    if game_active == False:
        screen.fill((200,200,200))#the numbers mean colors
        screen.blit(player_stand,player_stand_rect)
        screen.blit(intro_text,intro_rect)
        obstacle_rect_list.clear() #debug the colision to restart the game properly
       
        #these two following lines makes the character get back to the proper position when restarting the game
        player_rect.midbottom = (80,550)
        player_gravity = 0

        #screen.blit(player_stand,player_stand_rect)
    
    # elif game_active == 'game_over':

    #     game_over = pygame.transform.scale(game_over,(800,600))
    #     screen.blit(game_over,(0,0)) 

    #update 
    # everything
    pygame.display.update() #updating the display surface above
    clock.tick(60) #this '60' tells-me that my the while true loop shouldnt not run faster than 60fps
