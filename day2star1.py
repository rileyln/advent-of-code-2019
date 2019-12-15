# Author: Riley Lynn Nairn (she, her)
# Date: 2019 December 12
# Description: Advent of Code - Day Two, Star One


with open("/users/riley/downloads/day2star1.txt") as file:
    data = file.read()

gravity_assist_program = [num.strip() for num in data.split(",")]

print(gravity_assist_program)

gravity_assist_program = [int(num) for num in gravity_assist_program]

print(gravity_assist_program)

gravity_assist_program[1] = 12
gravity_assist_program[2] = 2

print(gravity_assist_program)

def intcode(opcode, index1, index2, out_index, collection):
    if opcode == 99:
        print("Opcode:",99)
        return False
    elif opcode == 1:
        print("Opcode:",1)
        collection[out_index] = collection[index1] + collection[index2]
        return True
    elif opcode == 2:
        print("Opcode:",2)
        collection[out_index] = collection[index1] * collection[index2]
        return True
    else:
        print("This is not a valid opcode:",opcode)
        return False

for num in range(0,len(gravity_assist_program),4):
    print("Index:",num)
    if not intcode(gravity_assist_program[num], gravity_assist_program[num + 1],
            gravity_assist_program[num + 2], gravity_assist_program[num + 3], gravity_assist_program):
        break
    # print(gravity_assist_program)

print(gravity_assist_program)