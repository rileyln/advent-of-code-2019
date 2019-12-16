# Author: Riley Lynn Nairn (she, her)
# Date: 2019 December 15
# Description: Advent of Code - Day Four, Star Two


def digits_not_decreasing(number):
    number_string = str(number)
    for digit in range(0, len(number_string)):
        if digit == len(number_string) - 1:
            return True
        else:
            if number_string[digit] > number_string[digit + 1]:
                return False


def only_two_adjacent_same_digits(number):
    number_string = str(number)
    previous_digit = number_string[0]
    digit_groups = {
        "0" : 0,
        "1" : 0,
        "2" : 0,
        "3" : 0,
        "4" : 0,
        "5" : 0,
        "6" : 0,
        "7" : 0,
        "8" : 0,
        "9" : 0
    }
    for digit in range(1, len(number_string)):
        if number_string[digit] == previous_digit:
            digit_groups[number_string[digit]] += 1
        else:
            previous_digit = number_string[digit]
    for digit in digit_groups:
        if digit_groups[digit] == 1:
            return True
    return False


potential_passwords = set()

for password in range(254032, 789860):
    if digits_not_decreasing(password) and only_two_adjacent_same_digits(password):
        potential_passwords.add(password)

print(len(potential_passwords))