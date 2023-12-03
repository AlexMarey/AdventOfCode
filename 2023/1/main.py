import re

search = ["one", "two", "three", "four",
          "five", "six", "seven", "eight", "nine"]
nums = ["1", "2", "3", "4", "5", "6", "7", "8", "9",]
numbers = {1: "one", 2: "two", 3: "three", 4: "four",
           5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"}


def get_calibration_value(full_text):
    digits = re.sub(r'[a-z]', '', full_text.lower())
    digit_length = len(digits)
    if (digit_length < 1):
        return 0
    elif (digit_length == 1):
        return int(f'{digits}{digits}')
    elif (digit_length == 2):
        return int(f'{digits}')
    elif (digit_length > 2):
        return int(f'{digits[0]}{digits[digit_length-1]}')


def get_calibration_wih_written_numbers(full_text):
    # Tuple of index, Number/Written_Number
    result = []
    full_search = search + nums

    # Find all numbers as digits and written out
    for search_item in full_search:
        indexes = find_all(f'({search_item})', full_text)
        for index in indexes:
            if index != -1:
                result.append((index, search_item))

    size = len(result)
    lowest_index = (99999, 'N/A')
    highest_index = (-1, 'N/A')
    if size < 1:
        return 0
    elif size == 1:
        value = result[0][1]
        return int(f'{get_written_number(value)}{get_written_number(value)}')
    elif size >= 2:
        for value in result:
            if value[0] < lowest_index[0]:
                lowest_index = value
            if value[0] > highest_index[0]:
                highest_index = value
        return int(f'{get_written_number(lowest_index[1])}{get_written_number(highest_index[1])}')


def get_written_number(value):
    if value in nums:
        return int(value)
    else:
        return list(numbers.keys())[list(numbers.values()).index(value)]


def find_all(search_regex, input_text):
    return [m.start() for m in re.finditer(search_regex, input_text)]


if __name__ == "__main__":
    data = list()
    with open("input.txt") as input:
        for line in input:
            line = line.strip('\n')
            data.append(line)

    sum = 0
    for value in data:
        sum += get_calibration_value(value)

    print(f'No text sum: {sum}')

    sum = 0
    for value in data:
        guess = int(get_calibration_wih_written_numbers(value))
        print(f'{data.index(value) + 1}: {guess}')
        sum += guess

    print(f'With text sum {sum}')
