from turtle import width
import pygame
from sys import exit
import random
from random import randint,choice
from player import Player 
from ObstacleCorrection import Obstacle
from background import Background
from score import Score

#creating a timer
def display_timer(screen):

    current_time = int(pygame.time.get_ticks() /100) - start_time
    timer_surface = test_font.render(f'{current_time}',False,(64,64,64)) #curren_time NEED TO BE AN INT
    timer_rect = timer_surface.get_rect(topleft = (700,47))
    screen.blit(timer_surface,timer_rect)
    return current_time

def testing_score (player, obstacle_group):
    for obstacle in obstacle_group:
        if player.sprite.x == obstacle.rect.x:
            return True

    return False

def collision_sprite(): 
    if pygame.sprite.spritecollide(player.sprite,obstacle_group,False):#1sprite, 2group, boolean:checks if the sprite collides with the group will be destroyed or noit
    #this entire statment returns a list if doesnt collide with anything is gonna return an empity list
        obstacle_group.empty()
        return False
    else:
        return True
        
def create_obstacle(current_time, screen, obstacle_group):
        if current_time % 10 == 0 and len(obstacle_group) < 4 and  current_time != 0 :
            type = randint(0,3)
            if type <2:
                enemy = Obstacle('snake',screen)
            else:
                enemy = Obstacle('stirge',screen)
            obstacle_group.add(enemy)
            pygame.time.wait(100)
            #print(len(obstacle_group))
			
def delete_obstacles(obstacle_group):
	for obstacle in obstacle_group.copy():
		if obstacle.rect.x <= -100:
			obstacle_group.remove(obstacle)
			#print(len(obstacle_group))

#initializing pygame
pygame.init()

#Creating your screen and important variables
width = 800
height = 600
screen = pygame.display.set_mode((width,height)) #widht,height #(()) its a tuple
pygame.display.set_caption('MapleStory Wannabe') #setting the name of the game
clock = pygame.time.Clock()
test_font = pygame.font.Font('freesansbold.ttf',30) #font type and font size
game_active = False
start_time = 0
# music
bg_music = pygame.mixer.Sound('backgroudmusic.wav')
bg_music.set_volume(0.2)
sound_active = False

#score
points = Score(screen)

#Background
bg = Background(screen)

#GROUPS
player = pygame.sprite.GroupSingle() #this is a group single

#p1 = pygame.sprite.GroupSingle() #this is a group single
p1 = Player() #instancia de jogador
player.add(p1) #this is a sprite

obstacle_group = pygame.sprite.Group()
obstacle_group.add(Obstacle('snake',screen))

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

#timer
timer_surface = test_font.render('Timer: ', False, 'Black') #text you want to display, anti anliasing(False or True) , color
timer_rect = timer_surface.get_rect(topleft = (600,47 ))

#intro screen
player_stand = pygame.image.load('WalkKing\Stand.png').convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand,0,3)
#player_stand =pygame.transform.scale(player_stand,(200,150))
player_stand_rect = player_stand.get_rect(center = (400,325))

#intro texts
intro_text = test_font.render('Press Enter to start the game', False, 'Black')
intro_rect = intro_text.get_rect(center = (420,200))


while True:
    #print(game_active)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit() 

#inputs

        if game_active == True:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and p1.rect.bottom >= 550:
                    #player_gravity = -17
                    p1.gravity = -17
            
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
                    #bg_music = pygame.mixer.Sound('backgroudmusic.wav')
                    #bg_music.set_volume(0.2)
                    #bg_music.play(loops = -1) #plays the sound 4ever

                
    if game_active == True:
    #music
        if sound_active == False:
            bg_music.play(loops = -1)#plays the sound 4ever
            sound_active = True
    #background
        bg.background_animation()
        
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
        points.show_score()
        for obstacle in obstacle_group:
            if p1.rect.x == obstacle.rect.x:
                points.increment_score()
    
        print(points.actual_score)


        #timer
        screen.blit(timer_surface,timer_rect)
        current_time = display_timer(screen)

    #Drawingand updating the player class
        player.draw(screen)
        player.update()

    #Drawing and updating the Obstacle class
        create_obstacle(current_time, screen, obstacle_group)
        obstacle_group.update()
        delete_obstacles(obstacle_group)
        obstacle_group.draw(screen)
        
    #Colision 
        game_active = collision_sprite()

        #simulating the colision with the floor
        if p1.rect.bottom >= 550:
            p1.rect.bottom = 550
        

    if game_active == False:
        sound_active = False
        bg_music.stop()
        screen.fill(('White'))#the numbers mean colors
        screen.blit(player_stand,player_stand_rect)
        screen.blit(intro_text,intro_rect)
       
        #these two following lines makes the character get back to the proper position when restarting the game
        p1.rect.midbottom = (80,550)
        p1.gravity = 0

    #update 
    # everything
    pygame.display.update() #updating the display surface above
    clock.tick(60) #this '60' tells-me that my the while true loop shouldnt not run faster than 60fps
