import os
import sys
import math
import random
import pygame


#-----------------------------------------------------------------------------------------------------------------------
os.environ['SDL_VIDEO_CENTERED'] = '1'
RES = WIDTH, HEIGHT = 800, 600
FPS = 60
FONT_SIZE=20

#-----------------------------------------------------------------------------------------------------------------------
pygame.init()
pygame.display.set_caption("Space 01")

window = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.Font(None, FONT_SIZE)
running = True
print ("Start")
#-----------------------------------------------------------------------------------------------------------------------

def text():
    value = font.render("sd", True, pygame.Color('deeppink'))
    window.blit(value, (0, 0))


#-----------------------------------------------------------------------------------------------------------------------
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    window.fill('black')
    text()

    pygame.display.flip()
    clock.tick(FPS)
print("Exit")
pygame.quit()
sys.exit()
