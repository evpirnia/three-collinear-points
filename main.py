import sys
from point import Point
from line import Line

def getSlope(point1, point2):
    return round((point1.y - point2.y) / (point1.x - point2.x), 15)

def getLine(lines, slope):
    for line in lines:
        if line.slope == slope:
            return line

points = []
lines = []
slopes = []

if len(sys.argv) < 2:
    print("error: please enter CSV filename")
else:
    filename = sys.argv[1]
    with open(filename, "r") as inputfile:
        for line in inputfile:
            x, y = line.strip().split(",")
            newPoint = Point(x, y)
            points.append(newPoint)

for currentPoint in points:
    for nextPoint in points[1:]:
        if currentPoint != nextPoint:
            slope = getSlope(currentPoint, nextPoint)
            if slope not in slopes:
                newLine = Line(slope)
                newLine.addPoint(currentPoint)
                newLine.addPoint(nextPoint)
                lines.append(newLine)
                slopes.append(slope)
            else:
                existingLine = getLine(lines, slope)
                existingLine.addPoint(currentPoint)
                existingLine.addPoint(nextPoint)

counter = 1
with open("output.csv", "w") as output:
    for line in lines:
        if len(line.points) > 2:
            output.write(line.getOutput(counter))
            counter = counter + 1

print("Result outputted to output.csv")
