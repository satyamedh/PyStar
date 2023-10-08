from classes.datatypes.location import Location
from classes.node import AStarNode as Node


class AStarGrid:
    def __init__(self, start_location: Location, end_location: Location, start_grid: list[list[int]]):
        self.START = start_location
        self.END = end_location
        self.GRID_BASE = start_grid
        self.GRID = self.create_grid(self.GRID_BASE)

    def create_grid(self, grid: list[list[int]]):
        # The ID of a grid is just the index of the node in the grid
        counter = 0
        new_grid = []
        for y in range(len(grid)):
            new_grid.append([])
            for x in range(len(grid[y])):
                new_grid[y].append(Node(counter, Location(x, y), grid[y][x] == 1, Location(x, y) == self.START,
                                        Location(x, y) == self.END))
                counter += 1
        return new_grid
