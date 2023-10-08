from classes.algorithm import AStar
from classes.datatypes.location import Location
import pygame


SAMPLE_GRID = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [2, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 0, 0, 0, 0, 3, 1, 0],
    [0, 1, 0, 1, 1, 1, 1, 1, 0],
    [0, 1, 0, 1, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 1, 0, 0, 0],
]

ALLOW_DIAGONAL = True

algo = AStar(ALLOW_DIAGONAL)

algo.populate_grid(SAMPLE_GRID)
print(algo.GRID)

solution = algo.pathfind()
print([str(node) for node in solution])

# visualize the solution using pygame.
# white = traversable
# black = obstacle
# red = closed
# green = open
# blue = start/end
# yellow = solution

pygame.init()

cell_size = 10  # adjust this based on maze size
maze_width = len(SAMPLE_GRID[0]) * cell_size
maze_height = len(SAMPLE_GRID) * cell_size

screen = pygame.display.set_mode((maze_width, maze_height))

# colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)

# game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # draw the maze
    for y in range(len(SAMPLE_GRID)):
        for x in range(len(SAMPLE_GRID[y])):
            color = (blue if (SAMPLE_GRID[y][x] in [2, 3]) else (
                red if Location(x, y) in solution else (white if SAMPLE_GRID[y][x] == 0 else black)))
            pygame.draw.rect(screen, color, (x * cell_size, y * cell_size, cell_size, cell_size))

    pygame.display.flip()

pygame.quit()
