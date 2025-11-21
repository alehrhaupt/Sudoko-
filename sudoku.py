import pygame
# from sudoku_generator import SudokuGenerator

SCREEN_WIDTH  = 600
SCREEN_HEIGHT = 700

BOARD_SIZE = 540
BOARD_TOP  = 80
BOARD_LEFT = (SCREEN_WIDTH - BOARD_SIZE) // 2

FPS = 60

BACKGROUND_COL = (255, 255, 255)
GRID_COL = (0, 0, 0)
BOLD_GRID_COL = (0, 0, 0)
SELECTED_COL = (255, 0, 0)
TXT_COLOR = (0, 0, 0)
BUTTON_COL = (200, 200, 200)
BUTTON_HOVER_COL = (170, 170, 170)

TITLE_FONT_SIZE = 48
BUTTON_FONT_SIZE = 32
NUMBER_FONT_SIZE = 40

DIFFICULTY = {
    "easy": 30,
    "medium": 40,
    "hard": 50
}

def gen_start_screen():
     start_screen = pygame.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)
     pygame.draw.rect(screen, sudoku_start_bg.jpg, start_screen)





def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    running = True
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BG_COLOR)
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()


if __name__ == '__main__':
    main()

