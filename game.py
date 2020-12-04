import pygame
import random

import dimensions
from forms import S, Z, I, O, J, L, T
import grid_field

pygame.font.init()



# index 0 - 6 represent shape





def convert_shape_format(shape):
    pass


def valid_space(shape, grid):
    pass


def check_lost(positions):
    pass


def draw_text_middle(text, size, color, surface):
    pass


def clear_rows(grid, locked):
    pass


def draw_next_shape(shape, surface):
    pass


def main(win):

    shapes = [S, Z, I, O, J, L, T]
    shape_colors = [(0, 255, 0), (255, 0, 0), (0, 255, 255), (255, 255, 0), (255, 165, 0), (0, 0, 255), (128, 0, 128)]

    locked_positions = {}
    grid = grid_field.create_grid(locked_positions)

    change_piece = False
    run = True
    current_piece = grid_field.get_shape(shapes, shape_colors)
    next_shape = grid_field.get_shape(shapes, shape_colors)
    clock = pygame.time.Clock()
    fall_time = 0

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if pygame.key == pygame.K_LEFT:
                    if valid_space(current_piece, grid):
                        current_piece.x -= 1
                if pygame.key == pygame.K_RIGHT:
                    if valid_space(current_piece, grid):
                        current_piece.x += 1
                if pygame.key == pygame.K_UP:
                    if valid_space(current_piece, grid):
                        current_piece.y += 1
                if pygame.key == pygame.K_DOWN:
                    if valid_space(current_piece, grid):
                        current_piece.rotation += 1

        grid_field.draw_window(win, grid)


def main_menu():
    win = pygame.display.set_mode((dimensions.S_WIDTH, dimensions.S_HEIGHT))
    pygame.display.set_caption('Tetris')
    main(win)



main_menu()  # start game
