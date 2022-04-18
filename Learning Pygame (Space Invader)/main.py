import pygame
from pygame.constants import KEYUP

#Initialising Pygame
pygame.init()

#Creating the screen
screen = pygame.display.set_mode((800, 600))

#Title and icon
pygame.display.set_caption("Dogfight")
icon = pygame.image.load('swords.png')
pygame.display.set_icon(icon)

#Player
Airplane = pygame.image.load('OUR_Plane.png')
X_axis = 335
Y_axis = 0
X_change = 0
Y_change = 0

def airplane(x, y):
    screen.blit(Airplane, (x, y))

#Game loop
run = True
while run:
    #Updating screen color 
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        #Giving funtion to the X button
        if event.type == pygame.QUIT:
            run = False

        #WASD movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                X_change = -0.3
            if event.key == pygame.K_d:
                X_change = 0.3
            if event.key == pygame.K_w:
                Y_change = -0.3
            if event.key == pygame.K_s:
                Y_change = 0.3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d or event.key == pygame.K_s or event.key == pygame.K_w:
                X_change = 0
                Y_change = 0

    #Placing airplane
    X_axis += X_change
    Y_axis += Y_change

    if X_axis <= 0:
        X_axis = 0
    elif X_axis >= 672:
        X_axis = 672

    if Y_axis <= 0:
        Y_axis = 0
    elif Y_axis >= 472:
        Y_axis = 472

    airplane(X_axis, Y_axis)
    pygame.display.update()