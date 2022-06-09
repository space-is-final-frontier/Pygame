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
fps_rect = fps_counter.get_rect(topleft = (5, 5))


imp_surface_unflipped = pygame.image.load('Graphics/Imp/walk_1_mod.png').convert_alpha()
imp_surface = pygame.transform.flip(imp_surface_unflipped, True, False)
imp_rect = imp_surface.get_rect(bottomleft = (400, 300))


vik_surface = pygame.image.load('Graphics/Viking Axe/walk_1_mod.png').convert_alpha()
vik_rect = vik_surface.get_rect(bottomleft = (80, 300))


while True:
    
    for event in pygame.event.get():    #Exit code
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        #if event.type == pygame.MOUSEMOTION:
        #    print(vik_rect.collidepoint(event.pos))
    

    #Placing the background and "fps counter"
    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    screen.blit(fps_counter, fps_rect)


    #pygame.draw.line(screen, 'black', (0, 0), (800, 400), 10)
    #pygame.draw.line(screen, 'black', (0, 0), pygame.mouse.get_pos(), 10)
    #pygame.draw.ellipse(screen, 'gold', pygame.Rect(200, 300, 100, 100))


    #Placing the Imp enemy and moving it
    imp_rect.left += -3

    if imp_rect.right <= 0:
        imp_rect.left = 800

    screen.blit(imp_surface, imp_rect)


    #Placing the Viking Hero
    screen.blit(vik_surface, vik_rect)


    #print(vik_rect.colliderect(imp_rect))

    #mouse_pos = pygame.mouse.get_pos()
    #print(vik_rect.collidepoint(mouse_pos))

    #print(pygame.mouse.get_pressed())



    pygame.display.update()     #Updating the display surface
    clock.tick(60)
