from classes.algorithm import AStar
from classes.datatypes.location import Location
import pygame
from classes.exceptions import NoPathFound
import random

ALLOW_DIAGONAL = True

algo = AStar(ALLOW_DIAGONAL, True)

GRID_X = 1000
GRID_Y = 1000

while True:
    # create a random grid
    SAMPLE_GRID = [[random.choice([0, 0, 1, 1]) for _ in range(GRID_X)] for _ in range(GRID_Y)]
    SAMPLE_GRID[0][0] = 2
    SAMPLE_GRID[-1][-1] = 3

    algo.populate_grid(SAMPLE_GRID)

    try:
        solution = algo.pathfind()
        break
    except NoPathFound:
        print("No path found, trying again")

# visualize the solution using pygame.
# white = traversable
# black = obstacle
# red = closed
# green = open
# blue = start/end
# yellow = solution

pygame.init()

cell_size = 5  # adjust this based on maze size
maze_width = len(SAMPLE_GRID[0]) * cell_size
maze_height = len(SAMPLE_GRID) * cell_size

screen = pygame.display.set_mode((maze_width, maze_height))

# colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
green = (0, 255, 0)

COLORS = {
    0: white,
    1: black,
    2: blue,
    3: blue,
    4: red,
    5: yellow,
    6: green
}

grid = algo.GRID.GRID

# game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # draw the maze
    for y in range(len(SAMPLE_GRID)):
        for x in range(len(SAMPLE_GRID[y])):
            color = COLORS[int(grid[y][x])]
            pygame.draw.rect(screen, color, (x * cell_size, y * cell_size, cell_size, cell_size))

    pygame.display.flip()

pygame.quit()
