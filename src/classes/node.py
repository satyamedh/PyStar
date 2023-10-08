from src.classes.datatypes.location import Location


class AStarNode:
    def __init__(self, location: Location, start: bool = False, end: bool = False):
        # Constants
        self.LOCATION = location
        self.START = start
        self.END = end

        # Costs
        self.g = 0
        self.h = 0
        self.f = 0

        # Parent
        self.parent: Location = Location(-1, -1, True)

    def __eq__(self, other):
        return self.LOCATION == other.LOCATION

    def __str__(self):
        # The string representation of the node is the string representation of the location and the f cost
        return f"({self.LOCATION}) - {self.f}"
