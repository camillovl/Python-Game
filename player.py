import pygame

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