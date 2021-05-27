import pygame, math
from utils import red

class Enemy(object):
	def __init__(self):
		self.image = pygame.Surface((50, 50))
		self.image.fill(red)
		self.rect = self.image.get_rect()
		self.speed = 3

	def target_player(self, player):
		
		x_diff = (player.rect.x + player.rect.width/2) - (self.rect.x + self.rect.width/2)
		y_diff = (player.rect.y + player.rect.height/2) - (self.rect.y + self.rect.height/2)
				
		magnitude = math.sqrt(float(x_diff**2 + y_diff**2))
		numframes = int(magnitude/self.speed)
						
		xmove = x_diff/numframes
		ymove = y_diff/numframes

		self.rect.x += xmove
		self.rect.y += ymove
		
	def update(self, player:
		self.target_player(player)
		
