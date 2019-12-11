# Author: Riley Lynn Nairn (she, her)
# Date: 2019 December 10
# Description: Advent of Code - Day One, Star One


with open("/users/riley/downloads/day1star1.txt") as file:
    data = file.read()

modules = data.splitlines()

fuel = [int(mass) // 3 - 2 for mass in modules]

total = 0

for num in fuel:
    total += num

print(total)