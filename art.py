import sys
import pygame
from PIL import Image
input_word = str(input("Enter the word that will be used in the drawing: \n")).strip()
input_path = str(input("Enter the path of the image that will be used in the drawing: \n"))
WIDTH, HEIGHT = 800, 600
COLS, ROWS = 60, 40
FONT_SIZE = 18
FPS = 15
input_word = input_word + " "
lenght = input_word.__len__()
pos_x_1 = 10 
pos_y_1 = 10
pos_x_2 = 10
pos_y_2 = 30
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
running = True
clock = pygame.time.Clock()
while running:
    pos_x_1 = 10
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
    word_surface = pygame.font.SysFont('Impact', FONT_SIZE)
    for i in range(0,15):
        pos_x_1 += (FONT_SIZE * lenght)
        word_surface = word_surface.render(input_word, True, (255, 255, 255))
        screen.blit(word_surface, (pos_x_1, pos_y_1))
    pygame.display.flip()
