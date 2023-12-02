import re

search = ["one", "two", "three", "four", "five", "six", "seven", "eight" ,"nine"]
nums = ["1", "2", "3", "4", "5", "6", "7", "8", "9",]
numbers = {1: "one", 2: "two", 3: "three", 4:"four", 5: "five", 6:"six", 7:"seven", 8:"eight" ,9:"nine"}

def get_calibration_value(full_text):
    digits = re.sub(r'[a-z]', '', full_text.lower())
    digit_length = len(digits)
    if(digit_length < 1):
        return 0
    elif(digit_length == 1): 
        return int(f'{digits}{digits}')
    elif(digit_length == 2):
        return int(f'{digits}')
    elif(digit_length > 2):
        return int(f'{digits[0]}{digits[digit_length-1]}')
    
def get_calibration_wih_written_numbers(full_text):
    result = []
    full_search = search + nums
    for search_item in full_search: 
        index = full_text.find(search_item)
        if index != -1:
            result.push((index, search_item))

    size = len(result)
    if size < 1:
        return 0
    elif size == 1:
        value = result[0][1]
        return get_written_number(value)
    elif size == 2:
        return
    else:
        return

def get_written_number(value):
    if value in nums:
        return int(value)
    else:
        return list(numbers.keys())[list(numbers.values()).index(value)]

if __name__ == "__main__": 
    data = list()

    with open("sample2.txt") as input:
        for line in input: 
            line = line.strip('\n')
            data.append(line)
    
    sum = 0
    for value in data:
        sum += get_calibration_value(value)
    
    print(f'No text {sum}')

    sum = 0
    for value in data: 
        sum += get_calibration_wih_written_numbers(value)
