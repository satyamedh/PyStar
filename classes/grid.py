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

    def get_node(self, location: Location):
        # check if the location is valid
        if 0 <= location.X < len(self.GRID[0]) and 0 <= location.Y < len(self.GRID):
            return self.GRID[location.Y][location.X]
        else:
            raise Exception(f"Location {location} is not valid")

    def get_neighbors(self, node: Node):
        neighbors = []
        # Get the neighbors of the node
        for y in range(node.LOCATION.Y - 1, node.LOCATION.Y + 2):
            for x in range(node.LOCATION.X - 1, node.LOCATION.X + 2):
                # Get the current node
                current_node = self.get_node(Location(x, y))
                # Check if the node is valid, not an obstacle, and not the current node
                if (0 <= x < len(self.GRID[0]) and 0 <= y < len(self.GRID)
                        and current_node != node and not current_node.OBSTACLE):
                    neighbors.append(current_node)
        return neighbors
