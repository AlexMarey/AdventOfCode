MIN_RANGE = 372304
MAX_RANGE = 847060

def stringConverstion(val):
    return str(val)

def isSixDigits(val):
    return len(val) == 6

def doesContainDoubles(val):
    address = 1
    while (addressInRange(address)):
        char1 = val[address]
        char2 = val[address-1]
        if(isMatching(char1, char2)):
            return True
        address = address + 1
    return False

def doesNotDecrease(val):
    maxNumber = -1
    for char in val:
        char = int(char)
        if(char >= maxNumber):
            maxNumber = char
        else:
            return False
    return True

def isMatching(char1, char2):
    return char1 == char2

def addressInRange(val):
    return (val >= 0 and val < 6)

def checkForMultiples(pwd, address):
    nextAddress = address + 1
    if(nextAddress > 5):
        return 5
    elif(pwd[address] == pwd[nextAddress]):
        return checkForMultiples(pwd, nextAddress)
    else:
        return address

def getPasswordMultiples(pwd):
    address = 0
    lastMultAddress = address
    output = list()
    
    while (address < 5):
        lastMultAddress = checkForMultiples(pwd, address)
        if (not (lastMultAddress == address)):
            output.append(pwd[address:lastMultAddress+1])
        address = lastMultAddress + 1
    return output
        
def hasDouble(pwd):
    hasMult = False
    
    multiples = getPasswordMultiples(pwd)
    for item in multiples:
        if (len(item) == 2):
            hasMult = True
    return hasMult

if __name__ == "__main__":
    totalPasswordCount = 0
    password = MIN_RANGE
    while (password <= MAX_RANGE):
        password = str(password)
        if (isSixDigits(password) and doesNotDecrease(password)):
            if(hasDouble(password)):
                totalPasswordCount = totalPasswordCount + 1
        password = int(password) + 1
    print("Potential Passwords: {}".format(totalPasswordCount))
