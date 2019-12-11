# Author: Riley Lynn Nairn (she, her)
# Date: 2019 December 10
# Description: Advent of Code - Day One, Star Two


with open("/users/riley/downloads/day1star1.txt") as file:
    data = file.read()

modules = data.splitlines()

def calculate_fuel(mass):
    fuel = mass // 3 - 2
    if fuel <= 0:
        return 0
    else:
        return fuel + calculate_fuel(fuel)

fuel = [calculate_fuel(int(mass)) for mass in modules]

total = 0

for num in fuel:
    total += num

print(total)