import pygame
from variables import *
from sys import exit

pygame.init()   #Initialising pygame

screen = pygame.display.set_mode((WIDTH, HEIGHT))   #Creating the display surface
pygame.display.set_caption("Google Dino Pygame")    #Setting the caption

clock = pygame.time.Clock()    #Creating the clock object

text_font = pygame.font.Font('Font\Pixeltype.ttf', 45)  #

sky_surface = pygame.image.load('Graphics\Sky.png').convert()    
ground_surface = pygame.image.load('Graphics\Ground.png').convert()    
text_surface = text_font.render('FPS: 60', False, 'black')    

while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    screen.blit(sky_surface, (0, -25))
    screen.blit(ground_surface, (0, 230))
    screen.blit(text_surface, (5, 5))

    i += 1

    if i == 9:

        k = WALK_LIST[j]

        if j == 5:
            j = 0
        else:
            j += 1

        i = 0

    IMP_XPOS = IMP_XPOS + IMP_DX
    IMP_YPOS = IMP_YPOS + IMP_DY

    if IMP_XPOS <= -100:
        IMP_XPOS = 650

    imp_surface_unflipped = pygame.image.load('Graphics\Imp\walk_{}.png'.format(k))
    imp_surface = pygame.transform.flip(imp_surface_unflipped, True, False)

    screen.blit(imp_surface, (IMP_XPOS, IMP_YPOS))

    pygame.display.update()
    clock.tick(60)
