import pygame
# from sudoku_generator import SudokuGenerator

SCREEN_WIDTH  = 600
SCREEN_HEIGHT = 700

BOARD_SIZE = 540
BOARD_TOP  = 80
BOARD_LEFT = (SCREEN_WIDTH - BOARD_SIZE) // 2

FPS = 60

BG_COLOR = (255, 255, 255)
GRID_COLOR = (0, 0, 0)
BOLD_GRID_COLOR = (0, 0, 0)
SELECTED_COLOR = (255, 0, 0)
TEXT_COLOR = (0, 0, 0)
BUTTON_COLOR = (200, 200, 200)
BUTTON_HOVER_COLOR = (170, 170, 170)

TITLE_FONT_SIZE = 48
BUTTON_FONT_SIZE = 32
NUMBER_FONT_SIZE = 40

DIFFICULTY_REMOVED = {
    "easy": 30,
    "medium": 40,
    "hard": 50
}




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

