import math

testOneA = ["R75", "D30", "R83", "U83", "L12", "D49", "R71", "U7", "L72"]
testOneB = ["U62", "R66", "U55", "R34", "D71", "R55", "D58", "R83"]
testOneOutput = 159

testTwoA = ["R98","U47","R26","D63","R33","U87","L62","D20","R33","U53","R51"]
testTwoB = ["U98","R91","D20","R16","D67","R40","U7","R15","U6","R7"]
testTwoOutput = 135

def calcManhattanDistance(x, y):
    return abs(x) + abs(y)

def printManhattanDistance(val):
    print("Shorstest Manhattan Distance: {}".format(val))

def printStepDistance(val):
    print("Shortest Step Distance: {}".format(val))

def halfBoard(val):
    return int(val / 2)

def parsePath(path):
    xDir, yDir = getDirection(path[0])
    length = getLength(path[1:])
    return (xDir, yDir, length)
    
def getDirection(dir):
    if (dir.upper() == "U"):
        return (0,1)
    elif(dir.upper() == "R"):
        return (1,0)
    elif(dir.upper() == "D"):
        return (0,-1)
    elif(dir.upper() == "L"):
        return (-1,0)

def getLength(length):
    return int(length)

def overlapExists(otherWire, cell):
    if (cell == otherWire):
        return True
    return False

def readInWires():
    with open("input.txt") as input:
        wireA = input.readline()
        wireB = input.readline()
    wireA = parseWireStrings(wireA)
    wireB = parseWireStrings(wireB)
    return wireA, wireB

def parseWireStrings(wireString):
    wire = wireString.strip()
    paths = wire.split(',')
    return paths

def common_members(a, b):
    a_set = set(a)
    b_set = set(b)
    common = a_set & b_set
    if (common):
        return common

def updatePosition(x, xDir, y, yDir, length):
    x = x + xDir
    y = y + yDir
    length = length - 1
    return x, y, length

def unpackIntersection(cross):
    return cross[0], cross[1]

def isNotStart(cross):
    return not (cross[0] == 0 and cross[1] == 0)

def listLengthisEqual(listA, listB):
    return len(listA) == len(listB)

def calcShortestManhattanDistance(intersections):
    distance = 9999999999999999
    for cross in intersections:
        x, y = unpackIntersection(cross)
        
        if(isNotStart(cross)):
            newDistance = calcManhattanDistance(x, y)
            if newDistance < distance:
                distance = newDistance
    return distance
    
def selectMinStep(stepCounts):
    return min(stepCounts)

def addStepCounts(listOne, listTwo):
    return [listOne[i] + listTwo[i] for i in range(len(listOne))] 

def getStepCounts(wire, intersections, startX, startY):
    output = list()
    for cross in intersections:
        x = startX
        y = startY
        stepCount = 0
        for path in wire: 
            xDir, yDir, length = parsePath(path)
            while(length > 0):
                if ((x, y) == cross):
                    output.append(stepCount)
                else: 
                    stepCount = stepCount + 1
                x, y, length = updatePosition(x, xDir, y, yDir, length)
    return output

if __name__ == "__main__":    
    
    wireAInstructions, wireBInstructions = readInWires()

    wireA = list()
    wireB = list()
    intersections = list()

    wireADenote = 'a'
    wireBDenote = 'b'

    currentWire = wireADenote
    oppWire = wireBDenote

    startX = 0
    startY = 0

    # Find all intersections
    for wire in [wireAInstructions, wireBInstructions]:
        x = startX 
        y = startY

        for path in wire:
            xDir, yDir, length = parsePath(path)
            while(length > 0):
                if (currentWire == wireADenote):
                    wireA.append((x, y))
                elif (currentWire == wireBDenote):
                    wireB.append((x,y))
                x, y, length = updatePosition(x, xDir, y, yDir, length)

        currentWire = wireBDenote
        oppWire = wireADenote
    
    intersections = common_members(wireA, wireB)

    intersections.remove((startX,startY))
    distance = calcShortestManhattanDistance(intersections)

    printManhattanDistance(distance)

    stepDistanceWireA = getStepCounts(wireAInstructions, intersections, startX, startY)
    stepDistanceWireB = getStepCounts(wireBInstructions, intersections, startX, startY)

    if (listLengthisEqual(stepDistanceWireA, stepDistanceWireB)):
        totalSteps = addStepCounts(stepDistanceWireA, stepDistanceWireB)
        stepDistanceCount = selectMinStep(totalSteps)
        printStepDistance(stepDistanceCount)
    else:
        print("Step count lists are not equal!")

