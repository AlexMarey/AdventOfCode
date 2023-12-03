# game: [Game #, turn data]
def get_possible_games(game):
    id = game[0][5:]
    rounds = game[1].split('; ')

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


if __name__ == "__main__":
    data = list()
    with open("input.txt") as input:
        for line in input:
            line = line.strip('\n')
            game = line.split(': ')
            data.append(game)

    sum = 0
    for game in data:
        sum += get_possible_games(game)
    print(sum)
