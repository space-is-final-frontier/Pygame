#Importing the modules
import pygame
from sys import exit
from random import randint

class Viking(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        vik_walk_1 = pygame.transform.scale(pygame.image.load('Graphics/Viking Axe/walk_1_mod.png').convert_alpha(), (63, 90))
        vik_walk_2 = pygame.transform.scale(pygame.image.load('Graphics/Viking Axe/walk_2_mod.png').convert_alpha(), (63, 90))
        vik_walk_3 = pygame.transform.scale(pygame.image.load('Graphics/Viking Axe/walk_3_mod.png').convert_alpha(), (63, 90))
        vik_walk_4 = pygame.transform.scale(pygame.image.load('Graphics/Viking Axe/walk_4_mod.png').convert_alpha(), (63, 90))
        vik_walk_5 = pygame.transform.scale(pygame.image.load('Graphics/Viking Axe/walk_5_mod.png').convert_alpha(), (63, 90))
        vik_walk_6 = pygame.transform.scale(pygame.image.load('Graphics/Viking Axe/walk_6_mod.png').convert_alpha(), (63, 90))

        self.vik_walk = [vik_walk_1, vik_walk_2, vik_walk_3, vik_walk_4, vik_walk_5, vik_walk_6]
        self.vik_walk_index = 0

        vik_attack_1 = pygame.transform.scale(pygame.image.load('Graphics/Viking Axe/attack2_1_mod.png').convert_alpha(), (63, 90))
        vik_attack_2 = pygame.transform.scale(pygame.image.load('Graphics/Viking Axe/attack2_2_mod.png').convert_alpha(), (63, 99))
        vik_attack_3 = pygame.transform.scale(pygame.image.load('Graphics/Viking Axe/attack2_3_mod.png').convert_alpha(), (114, 90))
        vik_attack_4 = pygame.transform.scale(pygame.image.load('Graphics/Viking Axe/attack2_4_mod.png').convert_alpha(), (192, 90))
        vik_attack_5 = pygame.transform.scale(pygame.image.load('Graphics/Viking Axe/attack2_5_mod.png').convert_alpha(), (72, 87))
        vik_attack_6 = pygame.transform.scale(pygame.image.load('Graphics/Viking Axe/attack2_6_mod.png').convert_alpha(), (87, 90))

        self.vik_attack = [vik_attack_1, vik_attack_2, vik_attack_3, vik_attack_4, vik_attack_5, vik_attack_6]
        self.vik_attack_index = 0

        self.image = self.vik_walk[self.vik_walk_index]
        self.rect = self.image.get_rect(midbottom = (100, 300))
        self.gravity = 0
        self.timer = 120

    def viking_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 300:
            self.gravity = -20

        '''
        if keys[pygame.K_w] and self.rect.bottom >= 300 and self.timer <= 0:
            self.attack_animation()

        else:
            self.animation()
        '''

    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 300:
            self.rect.bottom = 300

    def animation(self):
        self.vik_walk_index += 0.11
        if self.vik_walk_index >= len(self.vik_walk):
            self.vik_walk_index = 0
        self.image = self.vik_walk[int(self.vik_walk_index)]
        self.rect = self.image.get_rect(center = (self.rect.centerx, self.rect.centery))

    def attack_animation(self):
        self.vik_attack_index += 0.15
        if self.vik_attack_index >= len(self.vik_attack):
            self.vik_attack_index = 0
        self.image = self.vik_attack[int(self.vik_attack_index)]
        self.rect = self.image.get_rect(center = (self.rect.centerx, self.rect.centery))
        #self.timer = 120

    def update(self):
        self.viking_input()
        self.apply_gravity()
        self.animation()
        #self.timer -= 1


class Obstacle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        imp_frame_1 = pygame.transform.scale(pygame.transform.flip(pygame.image.load('Graphics/Imp/walk_1_mod.png').convert_alpha(), True, False), (54, 90))
        imp_frame_2 = pygame.transform.scale(pygame.transform.flip(pygame.image.load('Graphics/Imp/walk_2_mod.png').convert_alpha(), True, False), (54, 90))
        imp_frame_3 = pygame.transform.scale(pygame.transform.flip(pygame.image.load('Graphics/Imp/walk_3_mod.png').convert_alpha(), True, False), (54, 90))
        imp_frame_4 = pygame.transform.scale(pygame.transform.flip(pygame.image.load('Graphics/Imp/walk_4_mod.png').convert_alpha(), True, False), (54, 90))
        imp_frame_5 = pygame.transform.scale(pygame.transform.flip(pygame.image.load('Graphics/Imp/walk_5_mod.png').convert_alpha(), True, False), (54, 90))
        imp_frame_6 = pygame.transform.scale(pygame.transform.flip(pygame.image.load('Graphics/Imp/walk_6_mod.png').convert_alpha(), True, False), (54, 90))

        self.imp_frames = [imp_frame_1, imp_frame_2, imp_frame_3, imp_frame_4, imp_frame_5, imp_frame_6]
        self.imp_index = 0

        self.image = self.imp_frames[self.imp_index]
        self.rect = self.image.get_rect(midbottom = (randint(900, 1100), 300))

    def animation(self):
        self.imp_index += 0.11
        if self.imp_index >= len(self.imp_frames):
            self.imp_index = 0
        self.image = self.imp_frames[int(self.imp_index)]

    def destroy(self):
        if self.rect.x <= -100:
            self.kill

    def update(self):
        self.animation()
        self.rect.x -= 4
        self.destroy()


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

def collision_sprite():
    global game_active
    if pygame.sprite.spritecollide(viking.sprite, imp_group, False):
        imp_group.empty()
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
attack_timer = 0

#Groups
viking = pygame.sprite.GroupSingle()
viking.add(Viking())

imp_group = pygame.sprite.Group()

#Game variables
sky_surface = pygame.image.load('Graphics/Sky.png').convert()    #Loading the various surfaces
ground_surface = pygame.image.load('Graphics/Ground.png').convert()

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
            if event.type == obstacle_timer:
                imp_group.add(Obstacle())
            
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

        #Placing the Viking Hero
        viking.draw(screen)
        viking.update()

        imp_group.draw(screen)
        imp_group.update()

        #Collisions
        collision_sprite()

    else:
        screen.fill((94, 129, 162))
        screen.blit(intro_vik, intro_vik_rect)
        screen.blit(instruct, instruct_rect)

        end_score = text_font.render(f"Score: {score}", False, 'black')
        end_score_rect = end_score.get_rect(center = (400, 50))

        if score != 0:
            screen.blit(end_score, end_score_rect)

    pygame.display.update()     #Updating the display surface
    clock.tick(60)