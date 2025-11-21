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
BUTTON_COL = (255, 255, 200)
BUTTON_HOVER_COL = (170, 170, 170)
BUTTON_WIDTH = 200
BUTTON_HEIGHT = 60

TITLE_FONT_SIZE = 48
BUTTON_FONT_SIZE = 32
NUMBER_FONT_SIZE = 40

DIFFICULTY = {
    "easy": 30,
    "medium": 40,
    "hard": 50
}

def gen_start_screen(screen):
    start_screen = pygame.image.load('sudoku_start_bg.jpg')
    start_screen = pygame.transform.scale(start_screen, (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(start_screen,(0, 0))
    font = pygame.font.SysFont(None, TITLE_FONT_SIZE)
    title_surface = font.render("Welcome to Sudoku", True, TXT_COLOR)
    title_rect = title_surface.get_rect(center=(SCREEN_WIDTH//2, 150))
    screen.blit(title_surface, title_rect)
    select_mode_surface = font.render('SELECT GAME MODE:', True, TXT_COLOR)
    select_mode_rect = select_mode_surface.get_rect(center=(SCREEN_WIDTH//2, 300))
    screen.blit(select_mode_surface, select_mode_rect)






def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    running = True
    clock = pygame.time.Clock()
    easy_butt = pygame.Rect((SCREEN_WIDTH - BUTTON_WIDTH) // 2, 380, BUTTON_WIDTH, BUTTON_HEIGHT)
    medium_butt = pygame.Rect((SCREEN_WIDTH - BUTTON_WIDTH) // 2, 460, BUTTON_WIDTH, BUTTON_HEIGHT)
    hard_butt = pygame.Rect((SCREEN_WIDTH - BUTTON_WIDTH) // 2, 540, BUTTON_WIDTH, BUTTON_HEIGHT)
    button_font = pygame.font.SysFont(None, BUTTON_FONT_SIZE)


    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        gen_start_screen(screen)
        pygame.draw.rect(screen, BUTTON_COL, easy_butt)
        pygame.draw.rect(screen, BUTTON_COL, medium_butt)
        pygame.draw.rect(screen, BUTTON_COL, hard_butt)
        easy_txt = button_font.render('Easy', True, TXT_COLOR )

        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()


if __name__ == '__main__':
    main()

