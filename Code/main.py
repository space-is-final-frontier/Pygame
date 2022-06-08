#Importing the modules
import pygame
from variables import *
from sys import exit

pygame.init()   #Initialising pygame

screen = pygame.display.set_mode((WIDTH, HEIGHT))   #Creating the display surface, i.e. the screen the player will see
pygame.display.set_caption("Google Dino Pygame")    #Setting the caption

clock = pygame.time.Clock()    #Creating the clock object


text_font = pygame.font.Font('Font/Pixeltype.ttf', 45)  #Creating the font

sky_surface = pygame.image.load('Graphics/Sky.png').convert()    #Loading the various surfaces
ground_surface = pygame.image.load('Graphics/Ground.png').convert()

fps_counter = text_font.render('FPS: 60', False, 'black')   #Creating a fake fps counter


imp_surface_unflipped = pygame.image.load('Graphics/Imp/walk_1.png').convert_alpha()
imp_surface = pygame.transform.flip(imp_surface_unflipped, True, False)
imp_xpos = 400
imp_ypos = 175
imp_dx = -3

while True:
    
    for event in pygame.event.get():    #Exit code
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    screen.blit(fps_counter, (5, 5))


    imp_xpos += imp_dx

    if imp_xpos <= -100:
        imp_xpos = 800

    screen.blit(imp_surface, (imp_xpos, imp_ypos))


    pygame.display.update()     #Updating the display surface
    clock.tick(60)
