# Line class

class Line():
    def __init__(self, slope):
        self.slope = slope
        self.points = []
        self.output = ""
    def __add__(self, newPoint):
        if len(self.points) == 0:
            return True
        for p in self.points:
            if p.x == newPoint.x:
                if p.y == newPoint.y:
                    return False
        return True
    def addPoint(self, newPoint):
        if self.__add__(newPoint) == True:
            self.output += ("," + str(newPoint.x) + "," + str(newPoint.y))
            self.points.append(newPoint)
    def getOutput(self, line_ID):
        self.output = str(line_ID) + self.output + "\n"
        return self.output
