from classes.grid import AStarGrid as Grid
from typing import List
from classes.exceptions import InvalidBaseGrid
from classes.datatypes.location import Location
from classes.exceptions import NoPathFound

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
                    # Check if the value is the start or end node and set the location accordingly
                    if grid[y][x] == 2:
                        start.set_location(x, y)
                        grid[y][x] = 0
                        continue
                    elif grid[y][x] == 3:
                        end.set_location(x, y)
                        grid[y][x] = 0
                        continue
                    raise InvalidBaseGrid(f"Invalid value {grid[y][x]} at ({x}, {y})")

        # Make sure the start and end nodes were found
        if start.NOT_SET:
            raise InvalidBaseGrid("Start node not found")
        elif end.NOT_SET:
            raise InvalidBaseGrid("End node not found")

        # Create the grid
        self.GRID = Grid(start, end, grid)

    def sort_open(self):
        # Sort the open list by f cost
        self.OPEN.sort(key=lambda node: node.f)

    def pathfind(self):
        # Make sure the grid is populated
        if self.GRID is None:
            raise Exception("Grid not populated")

        # Add the start node to the open list
        self.OPEN.append(self.GRID.get_node(self.GRID.START))

        # Loop until the open list is empty
        while len(self.OPEN):
            # Get the node with the lowest f cost
            self.sort_open()
            current_node = self.OPEN[0]

            # Remove the current node from the open list and add it to the closed list
            self.OPEN.remove(current_node)
            self.CLOSED.append(current_node)

            # Check if the current node is the end node
            if current_node.END:
                # Return the path from the end node to the start node
                return self.GRID.get_path(current_node)

            # Get the neighbors of the current node
            neighbors = self.GRID.get_neighbors(current_node)

            # Loop through the neighbors
            for neighbor in neighbors:
                # Check if the neighbor is in the closed list
                if neighbor in self.CLOSED:
                    continue

                # Calculate the costs of the neighbor
                neighbor.calculate_costs(self.GRID.START, self.GRID.END)

                # Check if the neighbor is in the open list
                if neighbor in self.OPEN:
                    # Check if the neighbor has a lower g cost than the current node
                    if neighbor.g < current_node.g:
                        # Set the parent of the neighbor to the current node
                        neighbor.parent = current_node.LOCATION
                else:
                    # Add the neighbor to the open list and set the parent to the current node
                    self.OPEN.append(neighbor)
                    neighbor.parent = current_node.LOCATION

        # Raise an exception if no path was found
        raise NoPathFound("No path found")






