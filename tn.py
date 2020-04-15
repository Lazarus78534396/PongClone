import pygame
import random
pygame.init()

y=200
y2=250
x2=398
white = (255,255,255)
red = (255,0,0)
vel = 15
vel2 = 15
win = pygame.display.set_mode((700,500))
pygame.display.set_caption('pong v1.1')
run = True
clock = pygame.time.Clock()

def redrawWindow():
	win = pygame.display.set_mode((700,500))


while run:
	clock.tick(27)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
	keys = pygame.key.get_pressed()
	if keys[pygame.K_UP] and y>8:
		y-=vel2
	if keys[pygame.K_DOWN] and y<390:
		y+=vel2
	
	x2+=vel
		
	if x2>=696 and x2>=350:
		x2-=vel
		vel = -vel
		


	if x2<=30 :
		vel = -vel
		x2+=vel
		

		



	pygame.draw.line(win,white,(350,0), (350,500), 4)
	pygame.draw.line(win,white,(696,0), (696,500), 4)
	pygame.draw.line(win,white,(0,2), (700,2), 4)
	pygame.draw.line(win,white,(0,496), (700,496), 4)
	pygame.draw.ellipse(win,white,(312,210,80,80),5)
	pygame.draw.rect(win,white,(0,y,30,100))
	pygame.draw.rect(win,red,(x2,y2,10,10))
	pygame.display.update()
	redrawWindow()
pygame.quit()