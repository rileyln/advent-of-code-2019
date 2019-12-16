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


def two_adjacent_same_digits(number):
    number_string = str(number)
    previous_digit = number_string[0]
    for digit in range(1, len(number_string)):
        if number_string[digit] == previous_digit:
            return True
        else:
            previous_digit = number_string[digit]
    return False


potential_passwords = set()

for password in range(254032, 789860):
    if digits_not_decreasing(password) and two_adjacent_same_digits(password):
        potential_passwords.add(password)

print(len(potential_passwords))