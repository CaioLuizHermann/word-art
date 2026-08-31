import sys
import pygame
import math
input_word = str(input("Enter the word that will be used in the drawing: \n")).strip()
input_path = str(input("Enter the path of the image that will be used in the drawing: \n")).strip('"')
WIDTH, HEIGHT = 800, 600
COLS, ROWS = 60, 40
FONT_SIZE = 30
counter = 0
FPS = 15
input_word = input_word + " "
lenght = input_word.__len__()
pos_x_1 = 10 
pos_y_1 = 10
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
img_surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
img = pygame.image.load(input_path)
img_transformed = pygame.transform.scale(img, (WIDTH, HEIGHT))
running = True
clock = pygame.time.Clock()
speed = 2
word_surface = pygame.font.SysFont('Impact', FONT_SIZE)
word_surface_render = word_surface.render(input_word, True, (255, 255, 255))
width_word = word_surface_render.get_width()
step = width_word + 2
quantity = math.ceil((WIDTH/step))+2
def generate_words(posy):
    for i in range(0,quantity):
        img_surface.blit(word_surface_render, ((pos_x_1)+i*step, posy))
while running:
    screen.fill((0, 0, 0))
    img_frame = img_transformed.copy()
    screen.blit(img_frame, (0,0), special_flags=pygame.BLEND_RGBA_MULT)
    clock.tick(FPS)
    counter += speed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
    pos_x_1 = (counter % step) - step
    for j in range (-20, HEIGHT, 30):
        generate_words(j)
    img_surface.fill(0,0,0)
    pygame.display.flip()