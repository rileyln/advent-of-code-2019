# Author: Riley Lynn Nairn (she, her)
# Date: 2019 December 12
# Description: Advent of Code - Day Two, Star Two
import sys

with open("/users/riley/downloads/day2star1.txt") as file:
    data = file.read()

gravity_assist_template = [num.strip() for num in data.split(",")]

gravity_assist_template = [int(num) for num in gravity_assist_template]

print(gravity_assist_template)

print(len(gravity_assist_template))

def intcode_helper(opcode, index1, index2, out_index, collection):
    if opcode == 99:
        # print("Opcode:",99)
        return False
    elif opcode == 1:
        # print("Opcode:",1)
        collection[out_index] = collection[index1] + collection[index2]
        return True
    elif opcode == 2:
        # print("Opcode:",2)
        collection[out_index] = collection[index1] * collection[index2]
        return True
    else:
        print("This is not a valid opcode:", opcode)
        return False


def intcode(collection):
    for num in range(0, len(collection), 4):
        # print("Index:",num)
        if not intcode_helper(collection[num], collection[num + 1],
                              collection[num + 2], collection[num + 3], collection):
            break
    # print(collection)


for noun in range(0, 149):
    for verb in range(0, 149):
        gravity_assist_program = gravity_assist_template.copy()
        gravity_assist_program[1] = noun
        gravity_assist_program[2] = verb
        # print(gravity_assist_program)
        intcode(gravity_assist_program)
        if gravity_assist_program[0] == 19690720:
            print("Noun:", noun)
            print("Verb:", verb)
            print("100 * noun + verb =", 100 * noun + verb)
            break