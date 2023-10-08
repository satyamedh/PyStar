from src.classes.datatypes.location import Location


class AStarNode:
    def __init__(self, node_id: int, location: Location, obstacle: bool = False, start: bool = False, end: bool = False):
        # Constants
        self.LOCATION = location
        self.START = start
        self.END = end
        self.OBSTACLE = obstacle
        self.ID = node_id

        # Costs
        self.g = 0
        self.h = 0
        self.f = 0

        # Parent
        self.parent: Location = Location(-1, -1, True)

    def calculate_costs(self, start_node: Location, end_node: Location):
        if self.OBSTACLE:
            raise Exception(f"Cannot calculate costs for an obstacle {self.LOCATION} - {self.ID}")
        # Calculate the g cost
        self.g = self.LOCATION.distance(start_node)

        # Calculate the h cost
        self.h = self.LOCATION.distance(end_node)

        # Calculate the f cost
        self.f = self.g + self.h

    def __eq__(self, other):
        return self.LOCATION == other.LOCATION

    def __str__(self):
        # The string representation of the node is the string representation of the location and the f cost
        return f"({self.LOCATION}) - {self.f}"
