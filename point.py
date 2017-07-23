class Point():
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)
    def __eq__(self, other):
        if self.x == other.x:
            if self.y == other.y:
                return True
        return False
    def __ne__(self, other):
        if self.x == other.x:
            if self.y == other.y:
                return False
        return True
