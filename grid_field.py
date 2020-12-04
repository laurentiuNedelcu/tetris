from random import random
import pygame
import dimensions
from piece import Piece


def create_grid(locked_positions=None):

    if locked_positions is None:
        locked_positions = {}

    grid = [[(0, 0, 0) for _ in range(10)] for _ in range(20)]

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (j, i) in locked_positions:
                grid[i][j] = locked_positions[j, i]

    return grid


def draw_window(surface, grid):

    surface.fill((0, 0, 0))

    pygame.font.init()
    font = pygame.font.SysFont('helvetica', 60)
    label = font.render('Tetris', True, (255, 255, 255))

    surface.blit(label, (dimensions.TOP_LEFT_X + dimensions.PLAY_WIDTH/2 - label.get_width()/2), 30)

    draw_grid(surface, grid)

    pygame.display.update()


def draw_grid(surface, grid):

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            pygame.draw.rect(surface, grid[i][j], (dimensions.TOP_LEFT_X + j * dimensions.BLOCK_SIZE,
                                                   dimensions.TOP_LEFT_Y + i * dimensions.BLOCK_SIZE,
                                                   dimensions.BLOCK_SIZE,
                                                   dimensions.BLOCK_SIZE), 0)  # 0 to not draw a border

    pygame.draw.rect(surface, (255, 0, 0), (dimensions.TOP_LEFT_X, dimensions.TOP_LEFT_Y,
                                            dimensions.PLAY_WIDTH, dimensions.PLAY_HEIGHT), 4)


def get_shape(shapes, colors):
    shape = random.choice(shapes)
    return Piece(5, 0, shape, colors[shape])
