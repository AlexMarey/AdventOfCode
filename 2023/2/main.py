# game: [Game #, turn data]
def get_possible_games(game):
    id = game[0]
    rounds = game[1]

    for round in rounds:
        cubes_pulled = round.split(', ')
        for cubes in cubes_pulled:
            amount = 0
            if "red" in cubes:
                amount = int(cubes[:-4])
                if amount > 12:
                    return 0
            elif "blue" in cubes:
                amount = int(cubes[:-5])
                if amount > 14:
                    return 0
            elif "green" in cubes:
                amount = int(cubes[:-6])
                if amount > 13:
                    return 0
    return int(id)


def get_cubes_power(game):
    rounds = game[1]
    red = 0
    green = 0
    blue = 0
    for round in rounds:
        cubes_pulled = round.split(', ')
        for cubes in cubes_pulled:
            if "red" in cubes:
                red = compare_cubes(int(cubes[:-4]), red)
            elif "blue" in cubes:
                blue = compare_cubes(int(cubes[:-5]), blue)
            elif "green" in cubes:
                green = compare_cubes(int(cubes[:-6]), green)
    return red * green * blue


def compare_cubes(pulled, highest):
    if highest == 0:
        return pulled
    elif pulled > highest:
        return pulled
    return highest


if __name__ == "__main__":
    data = list()
    with open("input.txt") as input:
        for line in input:
            line = line.strip('\n')
            game = line.split(': ')
            game[0] = game[0][5:]
            game[1] = game[1].split('; ')
            data.append(game)

    sum = 0
    for game in data:
        sum += get_possible_games(game)
    print(f'Part 1: {sum}')

    power = 0
    for game in data:
        power += get_cubes_power(game)
    print(f'Part 2: {power}')
