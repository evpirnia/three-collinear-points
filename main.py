import sys
import argparse
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

parser = argparse.ArgumentParser()
parser.add_argument("-i", help="input file name")
parser.add_argument("-o", help="output file name", default="output.csv")
args = parser.parse_args()

if not args.i:
    print("error: please enter input CSV filename")
else:
    # reading input file contents
    with open(args.i, "r") as inputfile:
        for line in inputfile:
            x, y = line.strip().split(",")
            newPoint = Point(x, y)
            points.append(newPoint)
    # determining collinear points by obtaining slope between points
    for currentPoint in points:
        for nextPoint in points[1:]:
            if currentPoint != nextPoint:
                newSlope = getSlope(currentPoint, nextPoint)
                if newSlope not in slopes:
                    newLine = Line(newSlope)
                    newLine.addPoint(currentPoint)
                    newLine.addPoint(nextPoint)
                    lines.append(newLine)
                    slopes.append(newSlope)
                else:
                    existingLine = getLine(lines, newSlope)
                    existingLine.addPoint(currentPoint)
                    existingLine.addPoint(nextPoint)
    # writing results to output file
    counter = 1
    with open(args.o, "w") as outputfile:
        for line in lines:
            if len(line.points) > 2:
                outputfile.write(line.getOutput(counter))
                counter = counter + 1
    print "Result outputted to " + args.o
