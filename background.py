from turtle import width
import pygame
import math

class Background():
  def __init__(self,screen):

    self.screen = screen
    #self.clock = pygame.time.Clock()
    #self.FPS = 60

    self.widht = 800
    self.height = 600

    #create game window
    #self.screen = pygame.display.set_mode((self.widht, self.height))
    #pygame.display.set_caption("Endles Runner")

    #load image
    self.bg = pygame.image.load("bg.jpg").convert()
    self.bg_width = self.bg.get_width()
    self.bg_rect = self.bg.get_rect()

    #define game variables
    self.scroll = 0
    self.tiles = math.ceil(self.widht  / self.bg_width) + 1

    #game loop
    #self.run = True
    #while self.run:

  def background_animation(self):
      #self.clock.tick(self.FPS)

      #draw scrolling background
      for i in range(0, self.tiles):
        self.screen.blit(self.bg, (i * self.bg_width + scroll, 0))
        self.bg_rect.x = i * self.bg_width + scroll
        pygame.draw.rect(self.screen, (255, 0, 0), self.bg_rect, 1)

      #scroll background
      scroll -= 5

      #reset scroll
      if abs(scroll) > self.bg_width:
        scroll = 0

      #event handler
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          self.run = False

      #pygame.display.update()