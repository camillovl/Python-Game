from ast import increment_lineno
import pygame
import os

class Score():

    def __init__(self,screen):
        self.font = pygame.font.Font('freesansbold.ttf',70)
        self.screen = screen
        self.actual_score = None
        self.high_score = 0
        #self.score_message = self.font.render('PONTOS',False, 'Black')
        #self.score_message_rect = self.score_message.get_rect(topleft = (600 ,40))


    def show_score(self):
        
        #self.screen.blit(self.score_message,self.score_message_rect)

        self.score_value = self.font.render(f'{self.actual_score}',False,('Grey'))
        self.score_value_rect = self.score_value.get_rect(topleft = (400,300))
        self.screen.blit(self.score_value,self.score_value_rect)
    
    def increment_score (self):
        self.actual_score += 1
        


        if self.actual_score > self.high_score:
            self.actual_score = self.high_score