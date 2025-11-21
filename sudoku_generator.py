import math,random
import pygame
"""
This was adapted from a GeeksforGeeks article "Program for Sudoku Generator" by Aarti_Rathi and Ankur Trisal
https://www.geeksforgeeks.org/program-sudoku-generator/

"""

class SudokuGenerator:
    '''
	create a sudoku board - initialize class variables and set up the 2D board
	This should initialize:
	self.row_length		- the length of each row
	self.removed_cells	- the total number of cells to be removed
	self.board			- a 2D list of ints to represent the board
	self.box_length		- the square root of row_length

	Parameters:
    row_length is the number of rows/columns of the board (always 9 for this project)
    removed_cells is an integer value - the number of cells to be removed

	Return:
	None
    '''
    def __init__(self, row_length, removed_cells):
        self.row_length = row_length
        self.removed_cells = removed_cells
        self.board = [[0 for col in range(row_length)] for row in range(row_length)]
        self.box_length = int(math.sqrt(row_length))

    '''
	Returns a 2D python list of numbers which represents the board

	Parameters: None
	Return: list[list]
    '''
    def get_board(self):
        return self.board

    '''
	Displays the board to the console
    This is not strictly required, but it may be useful for debugging purposes

	Parameters: None
	Return: None
    '''
    def print_board(self):
        for row in self.board: #prints row
            print(row)

    '''
	Determines if num is contained in the specified row (horizontal) of the board
    If num is already in the specified row, return False. Otherwise, return True

	Parameters:
	row is the index of the row we are checking
	num is the value we are looking for in the row
	
	Return: boolean
    '''
    def valid_in_row(self, row, num):
        for col in range(self.row_length): #loop left to right
            if self.board[row][col] == num:
                return False

        return True

    '''
	Determines if num is contained in the specified column (vertical) of the board
    If num is already in the specified col, return False. Otherwise, return True

	Parameters:
	col is the index of the column we are checking
	num is the value we are looking for in the column
	
	Return: boolean
    '''
    def valid_in_col(self, col, num):
        for row in range(self.row_length): #loop top to bottom
            if self.board[row][col] == num:
                return False
        return True

    '''
	Determines if num is contained in the 3x3 box specified on the board
    If num is in the specified box starting at (row_start, col_start), return False.
    Otherwise, return True

	Parameters:
	row_start and col_start are the starting indices of the box to check
	i.e. the box is from (row_start, col_start) to (row_start+2, col_start+2)
	num is the value we are looking for in the box

	Return: boolean
    '''
    def valid_in_box(self, row_start, col_start, num):
        for row in range(row_start, row_start+3): #loop from start of row to end
            for col in range(col_start, col_start+3): #loop from start of col to end
                if self.board[row][col] == num: #if the num being checked equals num then False
                    return False
        return True
    
    '''
    Determines if it is valid to enter num at (row, col) in the board
    This is done by checking that num is unused in the appropriate, row, column, and box

	Parameters:
	row and col are the row index and col index of the cell to check in the board
	num is the value to test if it is safe to enter in this cell

	Return: boolean
    '''
    def is_valid(self, row, col, num):
        if not self.valid_in_row(row, num):
            return False
        if not self.valid_in_col(col, num):
            return False

        box_row_start = (row // 3) * 3
        box_col_start = (col // 3) * 3

        if not self.valid_in_box(box_row_start, box_col_start, num):
            return False

        return True

    '''
    Fills the specified 3x3 box with values
    For each position, generates a random digit which has not yet been used in the box

	Parameters:
	row_start and col_start are the starting indices of the box to check
	i.e. the box is from (row_start, col_start) to (row_start+2, col_start+2)

	Return: None
    '''
    def fill_box(self, row_start, col_start):
        numbers = [1,2,3,4,5,6,7,8,9]
        random.shuffle(numbers)

        index = 0
        for row in range(row_start, row_start+3):
            for col in range(col_start, col_start+3):
                self.board[row][col] = numbers[index]
                index += 1

    
    '''
    Fills the three boxes along the main diagonal of the board
    These are the boxes which start at (0,0), (3,3), and (6,6)

	Parameters: None
	Return: None
    '''
    def fill_diagonal(self):
        for i in range(0, self.row_length, self.box_length):
            self.fill_box(i, i)


    '''
    DO NOT CHANGE
    Provided for students
    Fills the remaining cells of the board
    Should be called after the diagonal boxes have been filled
	
	Parameters:
	row, col specify the coordinates of the first empty (0) cell

	Return:
	boolean (whether or not we could solve the board)
    '''
    def fill_remaining(self, row, col):
        if (col >= self.row_length and row < self.row_length - 1):
            row += 1
            col = 0
        if row >= self.row_length and col >= self.row_length:
            return True
        if row < self.box_length:
            if col < self.box_length:
                col = self.box_length
        elif row < self.row_length - self.box_length:
            if col == int(row // self.box_length * self.box_length):
                col += self.box_length
        else:
            if col == self.row_length - self.box_length:
                row += 1
                col = 0
                if row >= self.row_length:
                    return True
        
        for num in range(1, self.row_length + 1):
            if self.is_valid(row, col, num):
                self.board[row][col] = num
                if self.fill_remaining(row, col + 1):
                    return True
                self.board[row][col] = 0
        return False

    '''
    DO NOT CHANGE
    Provided for students
    Constructs a solution by calling fill_diagonal and fill_remaining

	Parameters: None
	Return: None
    '''
    def fill_values(self):
        self.fill_diagonal()
        self.fill_remaining(0, self.box_length)

    '''
    Removes the appropriate number of cells from the board
    This is done by setting some values to 0
    Should be called after the entire solution has been constructed
    i.e. after fill_values has been called
    
    NOTE: Be careful not to 'remove' the same cell multiple times
    i.e. if a cell is already 0, it cannot be removed again

	Parameters: None
	Return: None
    '''
    def remove_cells(self):
        count_cells = self.removed_cells

        while count_cells > 0:
            row = random.randint(0, self.row_length - 1)
            col = random.randint(0, self.row_length - 1)

            if self.board[row][col] != 0:
                self.board[row][col] = 0
                count_cells -= 1


class Cell:
    def __init__(self,  value, row, col, screen):
        self.value = value
        self.sketched_value = 0
        self.row = row
        self.col = col
        self.screen = screen
        self.selected = False
        self.square = pygame.Rect(self.row, self.col, 20, 20) #this creates individual cell squares(IDK what size to make them)
        self.font = pygame.font.Font(None, 36)

    def set_cell_value(self, value):
        self.value = value

    def set_sketched_value(self, value):
        self.sketched_value = value

    def draw(self):
        outline_color = (255, 0, 0) if self.selected else (0, 0, 0)
        pygame.draw.rect(self.screen, outline_color, self.square, 2)
        if self.value != 0:
            text_square = self.font.render(str(self.value), True, (0, 0, 0))
            self.screen.blit(text_square, text_square.get_rect(center=self.square.center))
            # this line should print the value that goes into the cell squares, pygame.font prints the value, text_surface is the box
            # which i think can be edited
        else:
            text_square = self.font.render(str(self.sketched_value), True, (0, 0, 0))
            self.screen.blit(text_square, text_square.get_rect(center=self.square.center))
            # this line should print empty squares when the value is = 0, pygame.font prints the value, text_surface is the box
            # which i think can be edited


'''
DO NOT CHANGE
Provided for students
Given a number of rows and number of cells to remove, this function:
1. creates a SudokuGenerator
2. fills its values and saves this as the solved state
3. removes the appropriate number of cells
4. returns the representative 2D Python Lists of the board and solution

Parameters:
size is the number of rows/columns of the board (9 for this project)
removed is the number of cells to clear (set to 0)

Return: list[list] (a 2D Python list to represent the board)
'''
def generate_sudoku(size, removed):
    sudoku = SudokuGenerator(size, removed)
    sudoku.fill_values()
    board = sudoku.get_board()
    sudoku.remove_cells()
    board = sudoku.get_board()
    return board

class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.rows = 9
        self.cols = 9
        self.full = False
    def draw(self):
        size_of_box = self.width // self.rows #may be wrong, check. Was thinking size of box will be determined by total width of board / self.row
        for i in range(self.rows + 1):
            if i%3 == 0:
                pygame.draw.line(self.screen, (0,0,0), (0, i * size_of_box), (self.width, i*size_of_box), 2) #horizontal
                pygame.draw.line(self.screen, (0,0,0), (i * size_of_box, 0), (i*size_of_box, self.height), 2)#vertical
            else:
                pygame.draw.line(self.screen, (0,0,0), (0, i * size_of_box), (self.width, i*size_of_box), 1) #horizontal
                pygame.draw.line(self.screen, (0,0,0), (i * size_of_box, 0), (i*size_of_box, self.height), 1)#vertical
    def select(self, row, col):
        self.selected_box = (row, col)
    def click(self, x, y):
        if 0<=x<self.width and 0<=y<self.height:
            size_of_box = self.width // self.rows
            row = y // size_of_box
            col = x // size_of_box # put row as y and col as x as a roy is vertical movement, thus y. Could make it wrong so check.
            return (row, col)
        else:
            return None
    def is_full(self):
        if self.full:
            return True
        return False














            




