import math

class Location:
    def __init__(self, x: int, y: int, not_set: bool = False):
        self.X = x
        self.Y = y
        self.NOT_SET = not_set

    def check_not_set(self):
        if self.NOT_SET:
            raise Exception("Location not set")

    def distance(self, other):
        self.check_not_set()
        other.check_not_set()

        # Distance formula: sqrt((x2 - x1)^2 + (y2 - y1)^2)
        return math.sqrt((other.X - self.X) ** 2 + (other.Y - self.Y) ** 2)

    def __eq__(self, other):
        return self.X == other.X and self.Y == other.Y

    def __str__(self):
        return f"({self.X}, {self.Y})"

