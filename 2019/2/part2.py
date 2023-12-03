part1 = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,9,1,19,1,9,19,23,1,23,5,27,2,27,10,31,1,6,31,35,1,6,35,39,2,9,39,43,1,6,43,47,1,47,5,51,1,51,13,55,1,55,13,59,1,59,5,63,2,63,6,67,1,5,67,71,1,71,13,75,1,10,75,79,2,79,6,83,2,9,83,87,1,5,87,91,1,91,5,95,2,9,95,99,1,6,99,103,1,9,103,107,2,9,107,111,1,111,6,115,2,9,115,119,1,119,6,123,1,123,9,127,2,127,13,131,1,131,9,135,1,10,135,139,2,139,10,143,1,143,5,147,2,147,6,151,1,151,5,155,1,2,155,159,1,6,159,0,99,2,0,14,0]

test1 = [1,0,0,0,99]

test2 = [2,3,0,3,99]

test3 = [2,4,4,5,99,0]

test4 = [1,1,1,4,99,5,6,0,99]

test5 = [1,9,10,3,2,3,11,0,99,30,40,50]

output = 19690720

def isEnd(code):
    if(code == 99):
        return True
    return False

def multiply(a, b):
    return a * b

def add(a, b): 
    return a + b

def nextInstruction(position):
    return position + 4

def getValue(code, position):
    return code[position]

def getAnswer(noun, verb):
    output = 100 * noun + verb
    print("Answer: {} ".format(output))
    print("Noun: {}\nVerb: {}".format(noun, verb))

def resetOpcode():
    return [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,9,1,19,1,9,19,23,1,23,5,27,2,27,10,31,1,6,31,35,1,6,35,39,2,9,39,43,1,6,43,47,1,47,5,51,1,51,13,55,1,55,13,59,1,59,5,63,2,63,6,67,1,5,67,71,1,71,13,75,1,10,75,79,2,79,6,83,2,9,83,87,1,5,87,91,1,91,5,95,2,9,95,99,1,6,99,103,1,9,103,107,2,9,107,111,1,111,6,115,2,9,115,119,1,119,6,123,1,123,9,127,2,127,13,131,1,131,9,135,1,10,135,139,2,139,10,143,1,143,5,147,2,147,6,151,1,151,5,155,1,2,155,159,1,6,159,0,99,2,0,14,0]

def solved(code):
    if(code[0] == output):
        print("Solved!")
        return True
    return False

if __name__ == '__main__':
    addInstruction = 1
    multiplyInstruction = 2
    
    noun = -1
    verb = -1

    solvedFlag = False

    for n in list(range(100)):
        for v in list(range(100)):

            # opcode = resetOpcode()
            # instructionAddress = 0
            # instruction = getValue(opcode, instructionAddress)
            
            if(not solvedFlag):

                opcode = resetOpcode()
                instructionAddress = 0
                instruction = getValue(opcode, instructionAddress)

                opcode[1] = n
                opcode[2] = v

                print("Testing noun={} and verb={}".format(opcode[1], opcode[2]))
                print("Initial opcode: {}".format(opcode))

                while(not isEnd(instruction)):
                    leftVarAddress = opcode[instructionAddress + 1]
                    rightVarAddress = opcode[instructionAddress + 2]
                    outputAddress = opcode[instructionAddress + 3]
                    
                    leftVar = opcode[leftVarAddress]
                    rightVar = opcode[rightVarAddress]
                    
                    if(instruction == addInstruction):
                        opcode[outputAddress] = add(leftVar, rightVar)
                    elif(instruction == multiplyInstruction):
                        opcode[outputAddress] =  multiply(leftVar, rightVar)
                    
                    instructionAddress = nextInstruction(instructionAddress)
                    instruction = getValue(opcode, instructionAddress)
                

                print("Final opcode: {}".format(opcode))
                print("Desired Value: {}".format(output))
                print("Final Value: {}\n".format(opcode[0]))

                if(solved(opcode)):
                    noun = n
                    verb = v
                    solvedFlag = True
    
    getAnswer(noun, verb)
