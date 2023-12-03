import math

def calculateFuel(mass):
    fuel = mass / 3
    fuel = math.floor(fuel)
    fuel = fuel - 2
    return fuel

def caluclateFuelForFuel(currentFuel):
    workingFuel = calculateFuel(currentFuel)
    print("Fuel req. for {} fuel: {}".format(currentFuel, workingFuel))
    if workingFuel < 0:
        print("Base case reached, returning zero")
        return 0
    print("Calling next level")
    return workingFuel + caluclateFuelForFuel(workingFuel)

if __name__ == "__main__":
    data = list()
    fuelRequired = 0

    with open("input.txt") as input:
        for line in input:
            line = line.strip('\n')
            data.append(int(line))
    
    for mass in data:
        fuel = calculateFuel(mass)
        extraFuel = caluclateFuelForFuel(fuel)
        fuelRequired = fuelRequired + fuel + extraFuel
        print("Initial Fuel: {}".format(fuel))
        print("Extra Fuel: {}".format(extraFuel))

    print("Final Fuel: {}".format(fuelRequired))