class Location:
    def __init__(self, x: int, y: int, not_set: bool = False):
        self.X = x
        self.Y = y

    def __eq__(self, other):
        return self.X == other.X and self.Y == other.Y

    def __str__(self):
        return f"({self.X}, {self.Y})"

