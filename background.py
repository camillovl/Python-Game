from turtle import width
import pygame
import math

class Background():
	def __init__(self,screen):

		self.screen = screen
		
		self.widht = 800
		self.height = 600
		
		
		#load image
		self.bg = pygame.image.load("bg.jpg").convert()
		self.bg_width = self.bg.get_width()
		self.bg_rect = self.bg.get_rect()
		
		#define game variables
		self.scroll = 0
		self.tiles = math.ceil(self.widht  / self.bg_width) + 1

	
	def background_animation(self):
		for i in range(0, self.tiles):
			self.screen.blit(self.bg, (i * self.bg_width + self.scroll, 0))
			self.bg_rect.x = i * self.bg_width + self.scroll
			#spygame.draw.rect(self.screen, (255, 0, 0), self.bg_rect, 1)
		
		#scroll background
		self.scroll -= 1.5
		
		#reset scroll
		if abs(self.scroll) > self.bg_width:
			self.scroll = 0
	
