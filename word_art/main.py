def main():
    import sys
    import pygame
    import math
    import argparse
    from colorama import Fore, Style, init
    from .startup import LOGO_RAW
    LOGO_COLOR = Fore.CYAN
    def print_side_by_side(gap=4): 
        logo_width = max(len(line) for line in LOGO_RAW)
        lines = [ f"{Fore.MAGENTA}{'Made by: CaioLuizHermann on GitHub'}",
        f"{Fore.CYAN}{'GitHub: https://github.com/CaioLuizHermann'}",
        f"{Fore.CYAN}{'Contact: caio_luiz_hermann@hotmail.com'}",
        f"{Fore.BLUE}{'-' * 50}",
        f"""{Fore.CYAN}{"Type 'word-art --help' for more info"}""", ]
        max_lines = max(len(LOGO_RAW), len(lines))
        for i in range(max_lines):
            rawline = LOGO_RAW[i] if i < len(LOGO_RAW) else ""
            infopart = lines[i] if i < len(lines) else ""
            padded_logo = rawline.ljust(logo_width)
            colored_logo = f"{LOGO_COLOR}{padded_logo}{Style.RESET_ALL}"
            print(f"{colored_logo}{' ' * gap}{infopart}")
    print_side_by_side()
    parser = argparse.ArgumentParser(prog="word-art",description=("This program is used to show a selected image with custom text"))
    parser.add_argument("-i","--image",default="./miku.png",required=False)
    parser.add_argument("-t","--text",default="MIKU",required=False)
    args = parser.parse_args()
    input_path = str(args.image).strip('"')
    input_word = str(args.text).strip('"')
    try:
        img = pygame.image.load(input_path)
    except:
        print("Error, invalid image path.")
        sys.exit()
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
        img_surface.fill((0,0,0,0))
        screen.fill((0, 0, 0))
        img_frame = img_transformed.copy()
        clock.tick(FPS)
        counter += speed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
        pos_x_1 = (counter % step) - step
        for j in range (-20, HEIGHT, 30):
            generate_words(j)
        img_frame.blit(img_surface, (0,0), special_flags=pygame.BLEND_RGBA_MULT)
        screen.blit(img_frame, (0,0))
        pygame.display.flip()
if __name__ == "__main__":
    main()