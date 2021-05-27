import pygame
from utils import *

class Player(object):
	def __init__(self):
		self.image = pygame.Surface((100,100))
		self.image.fill(blue)
		self.rect = self.image.get_rect()			

		self.rect.centerx = width/2
		self.rect.centery = height/2
		self.speed = 5
		
		self.ammo = []	
		self.bullets = []
		
		self.cooldown = 10
		self.cooldown_max = 10

		self.spawn_delay = 0
		self.spawn_delay_max = 30
		
	def move(self, dx, dy):
		self.rect.x += dx * self.speed
		self.rect.y += dy * self.speed
	
	def update(self, screen):
		pass
			
	def draw(self, surf):
		surf.blit(self.image, self.rect)

