#Importing the modules
import pygame
from sys import exit
from random import randint

def display_fps():
    fps = int(clock.get_fps())
    fps_counter = text_font.render(f'FPS: {fps}', False, 'black')
    fps_rect = fps_counter.get_rect(topleft = (5, 5))
    screen.blit(fps_counter, fps_rect)

def display_score():
    global score
    current_time = pygame.time.get_ticks() - start_time
    score = current_time // 1000
    score_counter = text_font.render(f'Score: {score}', False, (64, 64, 64))
    score_rect = score_counter.get_rect(center = (400, 50))
    screen.blit(score_counter, score_rect)

def imp_movement(imp_list):
    if imp_list:

        for imp_rect in imp_list:

            imp_rect.x -= 3.5

            screen.blit(imp_surface, imp_rect)
    
        imp_list = [imp_rect for imp_rect in imp_list if imp_rect.x > -50]

    return imp_list

def collisions(viking, imps_list):
    global game_active

    if imps_list:

        for imps_rect in imps_list:

            if viking.colliderect(imps_rect):

                game_active = False

pygame.init()   #Initialising pygame

#Global variables
screen = pygame.display.set_mode((800, 400))   #Creating the display surface, i.e. the screen the player will see
pygame.display.set_caption("Google Dino Pygame")    #Setting the caption
clock = pygame.time.Clock()    #Creating the clock object
text_font = pygame.font.Font('Font/Pixeltype.ttf', 45)  #Creating the font
game_active = False
start_time = 0
score = 0


#Game variables
sky_surface = pygame.image.load('Graphics/Sky.png').convert()    #Loading the various surfaces
ground_surface = pygame.image.load('Graphics/Ground.png').convert()


imp_surface = pygame.image.load('Graphics/Imp/ready_1_mod.png').convert_alpha()
imp_surface = pygame.transform.flip(imp_surface, True, False)
imp_surface = pygame.transform.scale(imp_surface, (54, 90))


imp_rect_list = []


vik_surface = pygame.image.load('Graphics/Viking Axe/ready_1_mod.png').convert_alpha()
vik_surface = pygame.transform.scale(vik_surface, (63, 90))
vik_rect = vik_surface.get_rect(bottomleft = (80, 300))
vik_gravity = 0


#Intro/End screen variables
intro_vik = pygame.image.load('Graphics/Viking Axe/ready_1.png').convert_alpha()
intro_vik = pygame.transform.scale(intro_vik, (200, 192))
intro_vik_rect = intro_vik.get_rect(center = (400, 200))


instruct = text_font.render("Press space bar to start the game", False, 'black')
instruct_rect = instruct.get_rect(center = (400, 350))


#Obstacles
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1500)


while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if vik_rect.collidepoint(event.pos) and vik_rect.bottom >= 290:
                    vik_gravity = -19
        
            if event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_SPACE, pygame.K_k, pygame.K_UP) and vik_rect.bottom >= 290:
                    vik_gravity = -19

                if event.key in (pygame.K_SPACE, pygame.K_k, pygame.K_UP) and vik_rect.bottom < 200:
                    vik_gravity -= 6
            
            if event.type == obstacle_timer:
                imp_rect_list.append(imp_surface.get_rect(bottomleft = (randint(900, 1100), 300)))
            
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                start_time = pygame.time.get_ticks()


    if game_active:
        #Placing the background and fps counter
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 300))
        display_score()
        display_fps()


        #Placing the Imp enemy and moving it
        imp_rect_list = imp_movement(imp_rect_list)


        #Placing the Viking Hero
        vik_gravity += 0.9
        vik_rect.y += vik_gravity

        if vik_rect.bottom >= 300:
            vik_rect.bottom = 300

        if vik_rect.top <= 0:
            vik_rect.top = 0

        screen.blit(vik_surface, vik_rect)


        #Collisions
        collisions(vik_rect, imp_rect_list)


    else:
        screen.fill((94, 129, 162))
        screen.blit(intro_vik, intro_vik_rect)
        screen.blit(instruct, instruct_rect)
        imp_rect_list.clear()

        vik_rect.bottom = 300
        vik_gravity = 0

        end_score = text_font.render(f"Score: {score}", False, 'black')
        end_score_rect = end_score.get_rect(center = (400, 50))

        if score == 0:
            pass
        else:
            screen.blit(end_score, end_score_rect)


    pygame.display.update()     #Updating the display surface
    clock.tick(60)
