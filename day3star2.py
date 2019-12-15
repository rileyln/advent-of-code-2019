# Author: Riley Lynn Nairn (she, her)
# Date: 2019 December 15
# Description: Advent of Code - Day Three, Star Two


class Wire:
    """

    """

    def __init__(self, coordinates):
        """

        """
        self.__coordinates = coordinates

        self.__last_coordinate = (0, 0)
        self.__grid = list()
        self.__grid.append(self.__last_coordinate)

        self.__convert_coordinates()

    def __convert_coordinates(self):
        for coordinate in self.__coordinates:
            direction = coordinate[0]
            distance = int(coordinate[1:])
            # print(coordinate, direction, distance)
            # print(self.__last_coordinate)

            if direction == "U":
                for y_coor in range(self.__last_coordinate[1] + 1, self.__last_coordinate[1] + distance + 1):
                    point_up_one = (self.__last_coordinate[0], y_coor)
                    # print(point_up_one)
                    self.__grid.append(point_up_one)
                    self.__last_coordinate = point_up_one
            elif direction == "D":
                for y_coor in range(self.__last_coordinate[1] - 1, self.__last_coordinate[1] - distance - 1, -1):
                    point_down_one = (self.__last_coordinate[0], y_coor)
                    # print(point_down_one)
                    self.__grid.append(point_down_one)
                    self.__last_coordinate = point_down_one
            elif direction == "L":
                for x_coor in range(self.__last_coordinate[0] - 1, self.__last_coordinate[0] - distance - 1, -1):
                    point_left_one = (x_coor, self.__last_coordinate[1])
                    # print(point_left_one)
                    self.__grid.append(point_left_one)
                    self.__last_coordinate = point_left_one
            elif direction == "R":
                for x_coor in range(self.__last_coordinate[0] + 1, self.__last_coordinate[0] + distance + 1):
                    point_right_one = (x_coor, self.__last_coordinate[1])
                    # print(point_right_one)
                    self.__grid.append(point_right_one)
                    self.__last_coordinate = point_right_one
            else:
                print("This is not a valid coordinate:", coordinate)

    def get_number_of_steps(self, point):
        for step in range(0, len(self.__grid)):
            if self.__grid[step] == point:
                return step

        return 9999999999

    def get_grid(self):
        return self.__grid


with open("/users/riley/downloads/day3star1.txt") as file:
    data = file.read()

wire1_and_wire2 = data.splitlines()

"""
with open("/users/riley/downloads/day3star1test.txt") as file:
    data = file.read()

wire1_and_wire2 = data.splitlines()
"""

wire1 = Wire([coordinate for coordinate in wire1_and_wire2[0].split(",")])
wire2 = Wire([coordinate for coordinate in wire1_and_wire2[1].split(",")])

# print(wire1.get_grid())
# print(wire2.get_grid())

wire1_set = set()
wire2_set = set()

for point in wire1.get_grid():
    wire1_set.add(point)
for point in wire2.get_grid():
    wire2_set.add(point)

intersections = wire1_set & wire2_set
intersections.remove((0, 0))


# print(intersections)

# print("Length of wire 1:", len(wire1.get_grid()))
# print("Length of wire 2:", len(wire2.get_grid()))
# print("Number of intersections:", len(intersections))

"""
def get_manhattan_distance(point):
    return abs(point[0]) + abs(point[1])


def get_shortest_distance(points):
    shortest_distance = 9999999999
    for point in points:
        # print(point)
        manhattan_distance = get_manhattan_distance(point)
        # print("Manhattan distance:",manhattan_distance)
        if manhattan_distance < shortest_distance:
            # print("Shorter:", manhattan_distance)
            shortest_distance = manhattan_distance
            closest_point = point
    return shortest_distance
"""


def get_distance_to_fastest_intersection(points):
    lowest_number_of_steps = 9999999999

    for intersection in points:
        steps_to_intersection = wire1.get_number_of_steps(intersection) + wire2.get_number_of_steps(intersection)
        if steps_to_intersection < lowest_number_of_steps:
            lowest_number_of_steps = steps_to_intersection

    return lowest_number_of_steps




print("Lowest number of steps:", get_distance_to_fastest_intersection(intersections))