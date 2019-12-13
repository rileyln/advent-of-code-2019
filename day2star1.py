# Author: Riley Lynn Nairn (she, her)
# Date: 2019 December 12
# Description: Advent of Code - Day Two, Star One


with open("/users/riley/downloads/day2star1.txt") as file:
    data = file.read()

gravity_assist_program = [num.strip() for num in data.split(",")]

print(gravity_assist_program)

gravity_assist_program[1] = 12
gravity_assist_program[2] = 2

print(gravity_assist_program)

def intcode(opcode, index1, index2, out_index, collection):
    if opcode == 99:
        return
    elif opcode == 1:
        collection[out_index] = index1 + index2
    elif opcode == 2:
        collection[out_index] = index1 * index2
    else:
        print("This is not a valid opcode.")