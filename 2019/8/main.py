WIDTH = 25
HEIGHT = 6

DATA_COUNT_IN_LAYER = WIDTH * HEIGHT

BLACK = "0"
WHITE = "1"
TRANSPARANT = "2"

def getData():
    with open("input.txt") as input:
        for line in input:
            line = line.strip('\n')
            data = line
    return data

def increment(val):
    return val + 1

def incWidthHeight(width, height):
    width = increment(width)
    if (width == WIDTH):
        width = 0
        height = increment(height)
    return width, height

def createLayer(val):
    return [[val for x in range(WIDTH)] for x in range(HEIGHT)]

def getLayer(data, layerLevel):
    layer = createLayer(0)
    curHeight = 0
    curWidth = 0
    address = layerLevel * DATA_COUNT_IN_LAYER
    
    while (curHeight < HEIGHT):
        layer[curHeight][curWidth] = data[address]
        address = increment(address)
        curWidth, curHeight = incWidthHeight(curWidth, curHeight)  
    return layer

def printLayer(level, layer):
    outputLine = ""
    curHeight = 0
    curWidth = 0
    
    print("Layer {}".format(str(level)))
    while (curHeight < HEIGHT):
        outputLine = outputLine + str(layer[curHeight][curWidth])
        curWidth = increment(curWidth)
        
        if (curWidth == WIDTH):
            print(outputLine)
            outputLine = ""
            curWidth = 0
            curHeight = increment(curHeight)
    
    print("-----")
    return

def printOutputLayer(layer):
    outputLine = ""
    curHeight = 0
    curWidth = 0
    
    while (curHeight < HEIGHT):
        outputLine = outputLine + str(layer[curHeight][curWidth])
        
        curWidth = increment(curWidth)
        
        if (curWidth == WIDTH):
            outputLine = outputLine + "\n"
            curWidth = 0
            curHeight = increment(curHeight)
    
    return outputLine

def getNumbers(num, layer):
    curHeight = 0
    curWidth = 0
    count = 0

    while (curHeight < HEIGHT):
        if (layer[curHeight][curWidth] == num):
            count = count + 1
        curWidth, curHeight = incWidthHeight(curWidth, curHeight)  
    
    return count
    
def getAnswerForPartOne(layers):
    answer = -1
    fewestZeros = 999999999
    for layer in layers:
        zeroCount = getNumbers("0", layer) 
        oneCount = getNumbers("1", layer) 
        twoCount = getNumbers("2", layer)
        
        if (zeroCount < fewestZeros):
            fewestZeros = zeroCount
            answer = oneCount * twoCount
    return answer

def getLayers(data):
    layers = list()
    currentLayer = 0
    totalLayers = int(len(data) / (WIDTH * HEIGHT))

    while(currentLayer < totalLayers):
        layers.append(getLayer(data, currentLayer))
        currentLayer = increment(currentLayer)
    return layers

def resetCurrentWidthHeight():
    return 0, 0

def makePicture(layers):
    output = createLayer(TRANSPARANT)
    curHeight, curWidth = resetCurrentWidthHeight()
    for layer in layers:
        while (curHeight < HEIGHT):
            if (output[curHeight][curWidth] == TRANSPARANT):
                if (layer[curHeight][curWidth] == BLACK):
                    output[curHeight][curWidth] = " "
                elif(layer[curHeight][curWidth] == WHITE):
                    output[curHeight][curWidth] = "X"
            curWidth, curHeight = incWidthHeight(curWidth, curHeight)
        
        curHeight, curWidth = resetCurrentWidthHeight()
    return output
            
def convertLayerToList(layer):
    output = ""
    curHeight = 0
    curWidth = 0
    for row in layer:
        output = output + "".join(row)
    return output

if __name__ == "__main__":
    data = getData()
    layers = getLayers(data)
    answer = getAnswerForPartOne(layers)
    print("Answer to Part 1: {}".format(answer))
    
    picture = makePicture(layers)
    printLayer("Answer to part 2", picture)
    
