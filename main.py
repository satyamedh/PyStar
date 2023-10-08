from classes.algorithm import AStar
from classes.datatypes.location import Location

# 3x3 grid with no obstacles
SAMPLE_GRID = [
    [0, 0, 2],
    [0, 1, 0],
    [3, 0, 0]
]

algo = AStar()

algo.populate_grid(SAMPLE_GRID)
print(algo.GRID)

solution = algo.pathfind()
print([str(node) for node in solution])

# visualize the solution using pygame. Convert the 1s to a black square and the 0s to a white square. Set all the
# values in the solution to a yellow square.

import pygame

pygame.init()

cell_size = 30  # adjust this based on maze size
maze_width = len(SAMPLE_GRID[0]) * cell_size
maze_height = len(SAMPLE_GRID) * cell_size

screen = pygame.display.set_mode((maze_width, maze_height))

# colors
white = (255, 255, 255)
black = (0, 0, 0)
yellow = (255, 255, 0)

# game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # draw the maze
    for y in range(len(SAMPLE_GRID)):
        for x in range(len(SAMPLE_GRID[y])):
            color = (yellow if Location(x, y) in solution else (white if SAMPLE_GRID[y][x] == 0 else black))
            pygame.draw.rect(screen, color, (x * cell_size, y * cell_size, cell_size, cell_size))

    pygame.display.flip()

pygame.quit()
