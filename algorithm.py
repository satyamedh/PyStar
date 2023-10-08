from classes.grid import AStarGrid as Grid
from typing import List
from classes.exceptions import InvalidBaseGrid
from classes.datatypes.location import Location


class AStar:
    def __init__(self):
        self.GRID = None
        self.OPEN = []
        self.CLOSED = []

    def populate_grid(self, grid: List[List[int]]):
        # The grid is a 2D list of integers, where 0 is a valid node and 1 is an obstacle.
        # The start node is represented by a 2, and the end node is represented by a 3.

        # Check if the grid is valid by checking if it is a 2D list
        if not isinstance(grid, list) or not isinstance(grid[0], list):
            raise InvalidBaseGrid("Grid must be a 2D list")

        start = Location(-1, -1, True)
        end = Location(-1, -1, True)
        # Make sure it only contains 0s, 1s, 2s, and 3s, simultaneously searching for the start and end nodes.
        for y in range(len(grid)):
            for x in range(len(grid[y])):
                if grid[y][x] not in [0, 1]:
                    raise InvalidBaseGrid(f"Invalid value {grid[y][x]} at ({x}, {y})")
                elif grid[y][x] == 2:
                    # We found the start node
                    start.set_location(x, y)
                    grid[y][x] = 0
                elif grid[y][x] == 3:
                    # We found the end node
                    end.set_location(x, y)
                    grid[y][x] = 0

        # Make sure the start and end nodes were found
        if start.NOT_SET:
            raise InvalidBaseGrid("Start node not found")
        elif end.NOT_SET:
            raise InvalidBaseGrid("End node not found")

        # Create the grid
        self.GRID = Grid(start, end, grid)




