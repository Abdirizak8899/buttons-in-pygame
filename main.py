"""
--------------------
Button using in pygame
fortionatly awesome
"""



import pygame as pyg ,random,sys
from pygame.locals import*
import BUTTON
from BUTTON import Button
widht,hight = 800,400

#screen
pyg.init()
screen = pyg.display.set_mode([widht,hight])
pyg.display.set_caption('button')

#buttons images
start_btn = pyg.image.load('start_btn.png').convert_alpha()
exit_btn = pyg.image.load('exit_btn.png').convert_alpha()


#buttons objects
start_buttom = Button(300,150-30,start_btn,0.8)
exit_buttom = Button(300+10,hight//2+50,exit_btn,0.8)

#variables
fps = pyg.time.Clock()
run = True

while run:
	screen.fill([200,120,200])

	#event handling
	for event in pyg.event.get():
		if event.type == QUIT:
			run = False

	# drawwing Buttons and making decisions
	if start_buttom.draw(screen):
		print('start')
	if exit_buttom.draw(screen):
		print('[+1] Game over')
		run = False
	pyg.display.update()
	fps.tick(60)
pyg.quit()