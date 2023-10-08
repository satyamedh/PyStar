from classes.grid import AStarGrid as Grid
from classes.node import AStarNode as Node
from typing import List
from classes.exceptions import InvalidBaseGrid
from classes.datatypes.location import Location
from classes.exceptions import NoPathFound
import copy


class AStar:
    def __init__(self):
        self.GRID: Grid = None
        self.OPEN = []
        self.CLOSED = []
        self.solved = False
        self.solution: List[Location] = []

    def populate_grid(self, grid: List[List[int]]):
        # The grid is a 2D list of integers, where 0 is a valid node and 1 is an obstacle.
        # The start node is represented by a 2, and the end node is represented by a 3.

        # We need to make a copy of the grid so that we don't modify the original grid
        grid = copy.deepcopy(grid)

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

        # Get the end node
        end_node = self.GRID.get_node(self.GRID.END)

        # Loop until the open list is empty
        while len(self.OPEN) > 0:
            # Sort the open list
            self.sort_open()
            # Get the node with the lowest f cost
            current = self.OPEN[0]
            self.OPEN.remove(current)
            self.CLOSED.append(current)

            if current == end_node:
                # We have found the end node
                self.solved = True
                self.solution = self.GRID.get_path(current)
                return self.solution

            # Get the neighbors of the current node
            neighbors: list[Node] = self.GRID.get_neighbors(current)
            for neighbor in neighbors:
                # Check if the neighbor is in the closed list, or if it is an obstacle
                if neighbor in self.CLOSED or neighbor.OBSTACLE:
                    continue

                    # check if the neighbor already has a parent, and if it does, check if the current node is a
                    # better parent
                if neighbor.parent.NOT_SET or neighbor.g > current.g + 1:
                    # Set the parent of the neighbor to the current node
                    neighbor.parent = current.LOCATION
                    # Calculate the costs of the neighbor
                    neighbor.calculate_costs(self.GRID.START, self.GRID.END)
                    # Add the neighbor to the open list if it is not already in it
                    if neighbor not in self.OPEN:
                        self.OPEN.append(neighbor)

        # Raise an exception if no path was found
        raise NoPathFound("No path found")

    def __str__(self):
        # There are three possible states for the algorithm:
        # 1. No grid has been populated - return "No grid populated"
        # 2. The grid has been populated but not solved - return the grid
        # 3. The grid has been populated and solved - return the grid with the path.
        # The solution is overlayed on the grid by replacing the values of the path with a #
        if self.GRID is None:
            return "No grid populated"
        elif not self.solved:
            return str(self.GRID)
        else:
            grid = str(self.GRID)
            for location in self.solution:
                grid = grid.replace(str(location), "#")
            return grid
