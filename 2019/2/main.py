forRealData = [1,12,2,3,
          1,1,2,3,
          1,3,4,3,
          1,5,0,3,
          2,9,1,19,
          1,9,19,23,
          1,23,5,27,
          2,27,10,31,
          1,6,31,35,
          1,6,35,39,
          2,9,39,43,
          1,6,43,47,
          1,47,5,51,
          1,51,13,55,
          1,55,13,59,
          1,59,5,63,
          2,63,6,67,
          1,5,67,71,
          1,71,13,75,
          1,10,75,79,
          2,79,6,83,
          2,9,83,87,
          1,5,87,91,
          1,91,5,95,
          2,9,95,99,
          1,6,99,103,
          1,9,103,107,
          2,9,107,111,
          1,111,6,115,
          2,9,115,119,
          1,119,6,123,
          1,123,9,127,
          2,127,13,131,
          1,131,9,135,
          1,10,135,139,
          2,139,10,143,
          1,143,5,147,
          2,147,6,151,
          1,151,5,155,
          1,2,155,159,
          1,6,159,0,99,
          2,0,14,0]

test1 = [1,0,0,0,99]

test2 = [2,3,0,3,99]

test3 = [2,4,4,5,99,0]

test4 = [1,1,1,4,99,5,6,0,99]

test5 = [1,9,10,3,2,3,11,0,99,30,40,50]

def isEnd(code):
    if(code == 99):
        print("End of the line!")
        return True
    return False

def returnPositionZero(opcode):
    return opcode[0]

def multiply(a, b):
    return a * b

def add(a, b): 
    return a + b

def nextOpline(position):
    return position + 4

if __name__ == '__main__':
    opcode = forRealData
    
    print("Initial State: {}".format(opcode))
    currentPosition = 0
    print("Next Opcode Slice: {}".format(opcode[currentPosition:currentPosition+4]))
    while(not isEnd(opcode[currentPosition])):
        # print("Current Position: {}".format(currentPosition))
        
        operation = opcode[currentPosition]
        leftVarPosition = opcode[currentPosition+1]
        rightVarPosition = opcode[currentPosition+2]
        desiredPosition = opcode[currentPosition+3]
        
        
        leftVar = opcode[leftVarPosition]
        rightVar = opcode[rightVarPosition]
        
        print("Operation: {}".format(operation))
        print("Variables: {}, {}".format(leftVar, rightVar))
        print("Desired Position: {}".format(desiredPosition))
        
        if(operation == 1):
            opcode[desiredPosition] = add(leftVar, rightVar)
            print("Adding Variables... New: {} at position {}".format(opcode[desiredPosition], desiredPosition))
        elif(operation == 2):
            opcode[desiredPosition] =  multiply(leftVar, rightVar)
            print("Multiplying Variables... New: {} at position {}".format(opcode[desiredPosition], desiredPosition))
        currentPosition = nextOpline(currentPosition)
        print("Opcode: {}".format(opcode))
        print("Next Opcode Slice: {}".format(opcode[currentPosition:currentPosition+4]))
        
    print("Final State: {}".format(opcode))