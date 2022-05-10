import pygame
from variables import *
from sys import exit
from animation import move

pygame.init()   #Initialising pygame

screen = pygame.display.set_mode((WIDTH, HEIGHT))   #Creating the display surface
pygame.display.set_caption("Google Dino Pygame")    #Setting the caption

clock = pygame.time.Clock()    #Creating the clock obimg_indect

text_font = pygame.font.Font('Font\Pixeltype.ttf', 45)  #Creating the font

sky_surface = pygame.image.load('Graphics\Sky.png').convert()    #Loading the various surfaces
ground_surface = pygame.image.load('Graphics\Ground.png').convert()    
fps_counter = text_font.render('FPS: 60', False, 'black')    


while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    screen.blit(fps_counter, (5, 5))

    IMP_XPOS, IMP_YPOS, frames, img, img_ind = move(IMP_XPOS, IMP_YPOS, IMP_DX, IMP_DY, frames, img, img_ind)

    if IMP_XPOS <= -100:
        IMP_XPOS = 800

    imp_surface_unflipped = pygame.image.load('Graphics\Imp\walk_{}.png'.format(img)).convert_alpha()
    imp_surface = pygame.transform.flip(imp_surface_unflipped, False, False)

    screen.blit(imp_surface, (IMP_XPOS, IMP_YPOS))

    pygame.display.update()
    clock.tick(60)
