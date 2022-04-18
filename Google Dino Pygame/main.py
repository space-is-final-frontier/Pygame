from cgi import test
from json import load
from matplotlib.pyplot import fill
import pygame
from sys import exit

pygame.init()

screen = pygame.display.set_mode((600, 300))
pygame.display.set_caption("Google Dino Pygame")
clock = pygame.time.Clock()

sky_surface = pygame.image.load('Google Dino Pygame/Graphics/Sky.png').convert()

while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    screen.blit(sky_surface, (0, 0))

    pygame.display.update()
    clock.tick(60)
