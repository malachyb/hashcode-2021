#!/usr/bin/env python3

from take_input import take_input
from street_input import street_input
from make_table import make_table
from intersection import intersection
from choose_light import choose
from progress import progress

def main():
    file = input()
    duration, intersections, streets, cars, bonus = take_input(file)

    list_intersections, dict_streets, list_cars = street_input(file, intersections, streets, cars)

    aidans_table = make_table(list_cars, dict_streets, duration)

    while len(aidans_table) > 1:
        intersections = {}
        for curr_street, curr_intersection in enumerate(aidans_table[0]):
            if curr_intersection not in intersections:
                intersections[curr_intersection] = [(curr_street, curr_intersection)]
            else:
                intersections[curr_intersection].append((curr_street, curr_intersection))

        dict_intersections = [intersection(row) for row in intersections.values()]

        light = [choose(dict_intersection) for dict_intersection in dict_intersections]

        aidans_table = progress(light, aidans_table)

if __name__ == '__main__':
    main()
