def get_first_digit(str):
    for char in str:
        if char.isdigit():
            return char
    return None

def get_last_digit(str):
    for char in reversed(str):
        if char.isdigit():
            return char
    return None

total = 0

with open('input.txt', 'r') as file:
    for line in file:
        combinedNr = get_first_digit(line) + get_last_digit(line)
        total += int(combinedNr)
        
print(total, end='')