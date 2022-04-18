import pygame
from sys import exit

pygame.init()

pygame.display.set_mode((800, 400))
pygame.display.set_caption("Learning Pygame")
clock = pygame.time.Clock()

while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    pygame.display.update()
    clock.tick(60)
