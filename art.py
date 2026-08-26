import sys
import pygame
import math
input_word = str(input("Enter the word that will be used in the drawing: \n")).strip()
input_path = str(input("Enter the path of the image that will be used in the drawing: \n"))
WIDTH, HEIGHT = 800, 600
COLS, ROWS = 60, 40
FONT_SIZE = 30
counter = 0
FPS = 15
input_word = input_word + " "
lenght = input_word.__len__()
pos_x_1 = 0
pos_y_1 = 0
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
running = True
clock = pygame.time.Clock()
speed = 2
def generate_words(pos_y):
    for i in range(0,quantity):
        screen.blit(word_surface_render, ((pos_x_1)+i*step, pos_y))
while running:
    screen.fill((0, 0, 0))
    clock.tick(FPS)
    counter += speed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
    word_surface = pygame.font.SysFont('Impact', FONT_SIZE)
    word_surface_render = word_surface.render(input_word, True, (255, 255, 255))
    width_word = word_surface_render.get_width()
    height_word = word_surface_render.get_height()
    step = width_word + 2
    step_ver = height_word + 2
    pos_x_1 = (counter % step) - step
    quantity = math.ceil((WIDTH/step))+2
    quantity_ver = math.ceil((HEIGHT/step_ver))+2
    for j in range(0, quantity_ver):
         generate_words(j * step_ver)
    pygame.display.flip()