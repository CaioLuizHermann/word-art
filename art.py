import sys
import pygame
from PIL import Image
import math
input_word = str(input("Enter the word that will be used in the drawing: \n")).strip()
input_path = str(input("Enter the path of the image that will be used in the drawing: \n"))
WIDTH, HEIGHT = 800, 600
COLS, ROWS = 60, 40
FONT_SIZE = 18
counter = 0
FPS = 15
input_word = input_word + " "
lenght = input_word.__len__()
pos_x_1 = 10 
pos_y_1 = 10
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
running = True
clock = pygame.time.Clock()
speed = 2
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
    step = width_word + 5
    quantity = math.ceil((WIDTH/step)+2)
    pos_x_1 = (counter % step) - step
    for i in range(0, quantity):
        screen.blit(word_surface_render, ((pos_x_1)+i*step, pos_y_1))
    pygame.display.flip()
