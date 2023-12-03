from data import partOne
from math import floor

ADD_INSTRUCTION = 1
MULTIPLY_INSTRUCTION = 2
INPUT_INSTRUCTION = 3
OUTPUT_INSTRUCTION = 4
JUMP_IF_TRUE_INSTRUCTION = 5
JUMP_IF_FALSE_INSTRUCTION = 6
LESS_THAN_INSTRUCTION = 7
EQUALS_INSTRUCTION = 8

POSITION_MODE = 0
IMMEDIATE_MODE = 1

def isEnd(code):
    if(code == 99):
        return True
    return False

def multiply(a, b):
    return a * b

def add(a, b): 
    return a + b

def getInput():
    # val = 1
    val = input("Your input is required: ")
    print("Testing Systems... beginning with System {}".format(val))
    return int(val)

def postOutput(val):
    print("Diagnostics Result: {}".format(val))
    return

def compareLessThan(var1, var2):
    if(var1 < var2):
        return 1
    return 0

def compareEquals(var1, var2):
    if(var1 == var2):
        return 1
    return 0

def jumpIfFalse(val):
    pass

def jumpIfTrue(val):
    pass

def getValue(code, position):
    return code[position]

def getVariables(instruction, opcode, instructionAddress, modes):
    if(instruction == ADD_INSTRUCTION or instruction == MULTIPLY_INSTRUCTION or instruction == EQUALS_INSTRUCTION or instruction == LESS_THAN_INSTRUCTION):
        if(modes[0] == POSITION_MODE):
            leftVarAddress = opcode[instructionAddress + 1]
            leftVar = opcode[leftVarAddress]
        else:
            leftVar = opcode[instructionAddress + 1]
        if(modes[1] == POSITION_MODE):
            rightVarAddress = opcode[instructionAddress + 2]
            rightVar = opcode[rightVarAddress]
        else:
            rightVar = opcode[instructionAddress + 2]
        return (leftVar, rightVar)
    elif(instruction == OUTPUT_INSTRUCTION or instruction == JUMP_IF_FALSE_INSTRUCTION or instruction == JUMP_IF_TRUE_INSTRUCTION):
        if(modes[0] == POSITION_MODE):
            varAdress = opcode[instructionAddress + 1]
            leftVar = opcode[varAdress]
        else:
            leftVar = opcode[instructionAddress + 1]
        return leftVar
    return None

def getOutputAddress(instruction, opcode, instructionAddress):
    if(instruction == ADD_INSTRUCTION or instruction == MULTIPLY_INSTRUCTION or instruction == EQUALS_INSTRUCTION or instruction == LESS_THAN_INSTRUCTION):
        return opcode[instructionAddress + 3] 
    elif(instruction == INPUT_INSTRUCTION):
        return opcode[instructionAddress + 1]
    elif(instruction == JUMP_IF_FALSE_INSTRUCTION or instruction == JUMP_IF_TRUE_INSTRUCTION):
        return opcode[instructionAddress + 2]
    return None

def processInstruction(instruction, instructionAddress, opcode, modes):
    variables = getVariables(instruction, opcode, instructionAddress, modes)
    outputAddress = getOutputAddress(instruction, opcode, instructionAddress)
    
    output = []
    if(instruction == ADD_INSTRUCTION):
        leftVar, rightVar = variables
        opcode[outputAddress] = add(leftVar, rightVar)
    elif(instruction == MULTIPLY_INSTRUCTION):
        leftVar, rightVar = variables
        opcode[outputAddress] = multiply(leftVar, rightVar)
    elif(instruction == INPUT_INSTRUCTION):
        opcode[outputAddress] = getInput()
    elif(instruction == OUTPUT_INSTRUCTION):
        postOutput(variables)
    elif(instruction == JUMP_IF_TRUE_INSTRUCTION):
        firstParam = variables
        if(firstParam != 0):
            if(modes[1] == POSITION_MODE):
                address = opcode[outputAddress]
            else:
                address = opcode[instructionAddress + 2]
            output.append(True)
            output.append(address)
        output.append(False)
    elif(instruction == JUMP_IF_FALSE_INSTRUCTION):
        firstParam = variables
        if(firstParam == 0):
            if(modes[1] == POSITION_MODE):
                address = opcode[outputAddress]
            else:
                address = opcode[instructionAddress + 2]
            output.append(True)
            output.append(address)
        output.append(False)
    elif(instruction == LESS_THAN_INSTRUCTION):
        leftVar, rightVar = variables
        opcode[outputAddress] = compareLessThan(leftVar, rightVar)
    elif(instruction == EQUALS_INSTRUCTION):
        leftVar, rightVar = variables
        opcode[outputAddress] = compareEquals(leftVar, rightVar)
    return output

def nextInstruction(position, instruction):
    # print(instruction)
    if(instruction == ADD_INSTRUCTION or instruction == MULTIPLY_INSTRUCTION or instruction == EQUALS_INSTRUCTION or instruction == LESS_THAN_INSTRUCTION):
        offset = 4
    elif(instruction == JUMP_IF_FALSE_INSTRUCTION or instruction == JUMP_IF_TRUE_INSTRUCTION):
        offset = 3
    elif(instruction == INPUT_INSTRUCTION or instruction == OUTPUT_INSTRUCTION):
        offset = 2
    return position + offset

def parseOpcode(opcode):
    instruction = opcode % 100
    hundredsDigit = floor((opcode / 100) % 10)
    thousandsDigit = floor((opcode / 1000) % 10)
    tenThousandsDigit = floor((opcode / 10000) % 10)
    return instruction, [hundredsDigit, thousandsDigit, tenThousandsDigit]

if __name__ == '__main__':
    opcode = partOne
    instructionAddress = 0
    instruction, modes = parseOpcode(opcode[instructionAddress])

    while(not isEnd(instruction)):
        result = processInstruction(instruction, instructionAddress, opcode, modes)
        if((instruction == JUMP_IF_FALSE_INSTRUCTION or instruction == JUMP_IF_TRUE_INSTRUCTION) and result[0] == True):
            instructionAddress = result[1]
        else:
            instructionAddress = nextInstruction(instructionAddress, instruction)
        instruction, modes = parseOpcode(opcode[instructionAddress])
