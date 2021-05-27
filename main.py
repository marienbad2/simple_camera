import pygame, random
from pygame.locals import *

from utils import *
from player import Player

pygame.init()

screen = pygame.display.set_mode(size)
pygame.display.set_caption("simple camera")
clock = pygame.time.Clock()

background = pygame.Surface(bg_size)

class Camera(object):
	def __init__(self, width, height):
		self.rect = pygame.Rect(0,0, width, height)
		self.width = width
		self.height = height
		
	def update(self, target):
		x = target.rect.centerx - int(width/2)
		y = target.rect.centery - int(height/2)
	
		# limit scrolling
		x = max(0, x) # left
		y = max(0, y) # top
	
		x = min((bg_width-width), x)
		y = min((bg_height-height), y)
		
		self.rect = pygame.Rect(x, y, self.width, self.height)

player = Player()
camera = Camera(width, height)
platforms = []

for i in range(50):
	x = random.randint(0, bg_width)
	y = random.randint(0, bg_height)
	
	w = random.randint(50, 100)
	h = 20
	
	s = pygame.Surface((w,h))
	s.fill(red)
	r = s.get_rect()
	r.x = x
	r.y = y
	
	platforms.append((s, r))
	background.blit(s, r)

running = True
while running:
	for event in pygame.event.get():
		
		if event.type == pygame.QUIT:
			running = False
	
	pressed = pygame.key.get_pressed()
			
	if pressed[pygame.K_LEFT]:
		player.move(-2, 0)

	if pressed[pygame.K_RIGHT]:
		player.move(2, 0)

	if pressed[pygame.K_UP]:
		player.move(0, -2)

	if pressed[pygame.K_DOWN]:
		player.move(0, 2)

	mouse = pygame.mouse.get_pressed()
	if mouse[0]:
		player.shoot()
	
	background.fill(black)

	for plat in platforms:
		background.blit(plat[0], plat[1])

	player.update(background)
	player.draw(background)
	camera.update(player)
	
	screen.blit(background, (0,0), camera.rect)

	player.rect.clamp_ip(background.get_rect())
	
	pygame.display.update()
	clock.tick(FPS)

pygame.quit()
quit()
