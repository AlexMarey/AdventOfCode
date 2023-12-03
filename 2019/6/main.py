class Node():
    def __init__(self, parent, name):
        #parent node
        self.parent = parent
        self.name = name
        if(parent is not None):
            self.count = parent.count + 1
        else: 
            self.count = 0

    def printNode(self):
        print("Name: {}".format(self.name)) 
        
        if(self.parent is not None):
            print("Parent: {}".format(self.parent.name))
        else:
            print("Parents: None")
        
        print("Count to base: {}\n".format(self.count))


def getData():
    output = list()
    with open("data.txt") as data:
        for line in data:
            line = line.strip('\n')
            output.append(line)
    return output

def parseOrbitString(data):
    output = data.split(')')
    return (output[0], output[1])

def parseOrbit(data):
    # Data 1 orbits Data 0
    return data[0], data[1]

def getOrbits(orbits):
    count = 0
    for s in orbits:
        count = count + s.count
    return count

def getAllOrbits(data):
    output = list()
    for item in data:
        orbit = parseOrbitString(item)
        output.append(orbit)
    return output

def getNextPointerPosition(p, length):
    p = p + 1
    if(p >= length):
        p = 0
    return p

def findNode(allNodes, nodeToFindByName):
    for item in allNodes:
        if (item.name == nodeToFindByName):
            return item
    return None

def find(masterList, name):
    for item in masterList:
        if(item == name):
            return item
    return None

if __name__ == '__main__':
    data = getData()

    allOrbits = getAllOrbits(data)
    orbitTree= [(Node(None, "COM"))]

    pointer = 0
    while(len(allOrbits) > 0):
        parentName, name = parseOrbit(allOrbits[pointer])        
        parent = findNode(orbitTree, parentName)

        if(parent):
            orbitTree.append(Node(parent, name))
            allOrbits.remove(allOrbits[pointer])

        pointer = getNextPointerPosition(pointer, len(allOrbits))
    
    print("All orbits: {}".format(getOrbits(orbitTree)))

    myShipOrbit = findNode(orbitTree, "YOU")
    santaShipOrbit = findNode(orbitTree, "SAN")
    
    myShipOrbit.printNode()
    santaShipOrbit.printNode()

    myOrbitPath = list()
    santaOrbitPath = list()
    
    commonParentFlag = False
    
    while(not commonParentFlag):
        print("Trying again: ")
        # Investigate parent orbit of me
        parentName = myShipOrbit.parent.name
        myOrbitPath.append(parentName)
        commonParent = find(santaOrbitPath, parentName)
        if(commonParent):
            commonParentFlag = True
        else:
            myShipOrbit = findNode(orbitTree, parentName)
    
        # investigate parent orbit of santa
        parentName = santaShipOrbit.parent.name
        santaOrbitPath.append(parentName)
        commonParent = find(myOrbitPath, parentName)

        # is there a common parent
        if(commonParent):
            commonParentFlag = True
        else:
            santaShipOrbit = findNode(orbitTree, parentName)

        print(myOrbitPath)
        print(santaOrbitPath)
    

    # count length of both listsi
    

