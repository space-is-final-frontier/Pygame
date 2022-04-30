import pygame
from sys import exit

pygame.init()

screen = pygame.display.set_mode((600, 300))
pygame.display.set_caption("Google Dino Pygame")
clock = pygame.time.Clock()
text_font = pygame.font.Font('Font\Pixeltype.ttf', 50)

sky_surface = pygame.image.load('Graphics\Sky.png').convert()
ground_surface = pygame.image.load('Graphics\Ground.png').convert()
text_surface = text_font.render('60', False, 'black')

imp_surface_unflipped = pygame.image.load('Graphics\Imp\walk_1.png')
imp_surface = pygame.transform.flip(imp_surface_unflipped, True, False)

while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    screen.blit(sky_surface, (0, -25))
    screen.blit(ground_surface, (0, 230))
    screen.blit(text_surface, (5, 5))
    screen.blit(imp_surface, (400, 150))

    pygame.display.update()
    clock.tick(60)
