import pygame
from sys import exit

class MarioWannabe:
    """Overall class with screen and important variables"""

    def __init__(self):
        """Initialize the game and create game resources"""
        pygame.init()

        pygame.display.set_caption('Jogo.png') #setting the name of the game

        self.screen = pygame.display.set_mode((1000,750)) #widht,height #(()) its a tuple
        self.clock = pygame.time.Clock()
        self.test_font = pygame.font.Font('pixeltype.ttf',30) #font type and font size
        self.game_active = False
        self.start_time = 0

    def display_score(self):
        """It not actual an score, it is a timer"""
        current_time = pygame.time.get_ticks() - self.start_time
        score_surface = self.test_font.render(f'{current_time}',False,(64,64,64)) #curren_time NEED TO BE AN INT
        score_rect = score_surface.get_rect(topleft = (425,50))
        self.screen.blit(score_surface,score_rect)
        #print(current_time)
    
    def sprite_sheet(self):
        """Overal sprites used in the game"""

        self.background_surface = pygame.image.load('backgrounds.png').convert_alpha() #converting an image to alpha facilitates pygame to read the code and make it lighter
        self.title0_surface = pygame.image.load('Tiles\Dois.png').convert_alpha()
        self.title1_surface = pygame.image.load('Tiles\Dois.png').convert_alpha()
        self.title2_surface = pygame.image.load('Tiles\Dois.png').convert_alpha()
        self.title3_surface = pygame.image.load('Tiles\Dois.png').convert_alpha()
        self.title4_surface = pygame.image.load('Tiles\Dois.png').convert_alpha()
        self.title5_surface = pygame.image.load('Tiles\Dois.png').convert_alpha()
        self.title6_surface = pygame.image.load('Tiles\Dois.png').convert_alpha()
        self.title7_surface = pygame.image.load('Tiles\Dois.png').convert_alpha()
        self.title8_surface = pygame.image.load('Tiles\Dois.png').convert_alpha()

        self.game_over = pygame.image.load('gameover.png')

    def score_rect(self):
        """Score surface with score rectangle"""
        self.score_surface = self.test_font.render('Score:', False, 'White') #text you want to display, anti anliasing(False or True) , color
        self.score_rect = self.score_surface.get_rect(topleft = (320,45 ))
    
    def enemies(self):
        """Snake surface with snake rectangle"""
        self.snake_surface = pygame.image.load('Snake\Cobra 1.png').convert_alpha()
        self.snake_rect = self.snake_surface.get_rect(bottomright = (600,605))

    def player(self):
        """Player surface with player rectangle"""
        self.player_surface = pygame.image.load('WalkSoldier\Soldado (1).png').convert_alpha()
        self.player_rect = self.player_surface.get_rect(midbottom = (200,605)) #get the player surface and draws an rectangle around
        #Gravity
        self.player_gravity = 0

    def intro_screen(self):
        """intro screen and intro texts"""
        #intro screen
        self.player_stand = pygame.image.load('WalkKing\Stand.png').convert_alpha()
        self.player_stand = pygame.transform.rotozoom(self.player_stand,0,3)
        #player_stand =pygame.transform.scale(player_stand,(200,150))
        self.player_stand_rect = self.player_stand.get_rect(center = (500,325))

        #intro texts
        intro_text = self.test_font.render('Press R to Start', False, 'Black')
        intro_rect = intro_text.get_rect(center = (500,200))

        #defining the color of the background (display surface)
        #test_surface = pygame.Surface((100,200))
        #test_surface.fill('Red')

    def run_game(self):
        """Main loop for the game"""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit() 

#inputs
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and self.player_rect.bottom >= 605:
                        player_gravity = -20
        
                # code to clik on the player to jump if necessary
                #if event.type == pygame.MOUSEBUTTONDOWN:
                    #if player_rect.collidepoint(event.pos):
                        #player_gravity = -20
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        game_active = True
                        self.snake_rect.left = 800
                        start_time = pygame.time.get_ticks()


            if game_active:
            #background
                self.screen.blit(self.background_surface,(0,0))
            #Ground
                self.screen.blit(self.title0_surface,(0,600))  #blit is used when you want to put a surface in another surface    
                self.screen.blit(self.title1_surface,(128,600))  #blit is used when you want to put a surface in another surface    
                self.screen.blit(self.title2_surface,(256,600))  #blit is used when you want to put a surface in another surface    
                self.screen.blit(self.title3_surface,(384,600))  #blit is used when you want to put a surface in another surface    
                self.screen.blit(self.title4_surface,(512,600))  #blit is used when you want to put a surface in another surface    
                self.screen.blit(self.title5_surface,(640,600))  #blit is used when you want to put a surface in another surface    
                self.screen.blit(self.title6_surface,(672,600))  #blit is used when you want to put a surface in another surface    
                self.screen.blit(self.title7_surface,(800,600))  #blit is used when you want to put a surface in another surface    
                self.screen.blit(self.title8_surface,(928,600))  #blit is used when you want to put a surface in another surface    
            #Score  
                pygame.draw.rect(self.screen,'Black',self.score_rect)
                self.screen.blit(self.score_surface,self.score_rect)

                #display_score()
                
            #Snake   
                self.snake_rect.x -= 3
                if self.snake_rect.right <= 0:
                    self.snake_rect.left = 1000
                #pygame.draw.rect(screen,'Red',snake_rect)
                self.screen.blit(self.snake_surface,(self.snake_rect))

            #player
                player_gravity += 1
                self.player_rect.y += player_gravity
                
                #simulating the colision with the floor
                if self.player_rect.bottom >= 605:
                    self.player_rect.bottom = 605
                #pygame.draw.rect(screen,'Blue',player_rect)
                self.screen.blit(self.player_surface,(self.player_rect))   

            #collision
                self.player_rect.colliderect(self.snake_rect)
                print(self.player_rect.colliderect(self.snake_rect)) #the moment rectangle colides it becames true
                
                #End the game if the player touches the snake
                if self.snake_rect.colliderect(self.player_rect):
                    game_active = False
            else:
                self.screen.fill((200,200,200))#the numbers mean colors
                self.screen.blit(self.player_stand,self.player_stand_rect)
                self.screen.blit(self.intro_text,self.intro_rect)
                #screen.blit(player_stand,player_stand_rect)
                #update everything
                pygame.display.update() #updating the display surface above
                self.clock.tick(60) #this '60' tells-me that my the while true loop shouldnt not run faster than 60fps



