from classes.datatypes.location import Location
from classes.node import AStarNode as Node
from classes.exceptions import NodeDoesntExist, InvalidLocation

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
            raise InvalidLocation(f"Location {location} is invalid")

    def get_neighbors(self, node: Node, allow_diagonal: bool = False):
        neighbors = []
        # Get the neighbors of the node
        for y in range(node.LOCATION.Y - 1, node.LOCATION.Y + 2):
            for x in range(node.LOCATION.X - 1, node.LOCATION.X + 2):
                # Check if the node is diagonal to the current node
                if not allow_diagonal and not (x == node.LOCATION.X or y == node.LOCATION.Y):
                    continue
                try:
                    current_node = self.get_node(Location(x, y))
                except InvalidLocation:
                    continue
                # Check if the node is valid, not an obstacle, and not the current node
                if current_node.LOCATION != node.LOCATION and not current_node.OBSTACLE:
                    neighbors.append(current_node)
        return neighbors

    def get_path(self, node: Node):
        path = []
        # Get the path from the given node to the start node
        while node.LOCATION != self.START:
            path.append(node.LOCATION)
            node = self.get_node(node.parent)
        path.append(self.START)
        return path

    def __str__(self):
        # Return the string representation of the grid as a 2D matrix of the node type
        return "\n".join([" ".join([str(node) for node in row]) for row in self.GRID])
