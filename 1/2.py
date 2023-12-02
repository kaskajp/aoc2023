words = ['1', '2', '3', '4', '5', '6', '7', '8', '9',
           'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

numbers = {
    '1': '1',
    '2': '2',
    '3': '3',
    '4': '4',
    '5': '5',
    '6': '6',
    '7': '7',
    '8': '8',
    '9': '9',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

def get_match(list, input_string, first_last):
    for i in list:
        if i not in input_string:
            continue
        if first_last == 0:
            yield i, input_string.index(i)
        elif first_last == 1:
            yield i, input_string.rindex(i)            

total = 0

with open('input.txt', 'r') as file:
    for line in file:
        first_index = 999
        first_match = ''
        for word, position in get_match(words, line, 0):
            if position <= first_index:
                first_index = position
                first_match = word

        last_index = 0
        last_match = ''
        for word, position in get_match(words, line, 1):
            if position >= last_index:
                last_index = position
                last_match = word

        if first_match != "" and last_match != "":
            combinedNumber = int(numbers[first_match] + "" + numbers[last_match])
            total += combinedNumber

print(total)
