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
        dict_intersections = intersection(aidans_table[0])

        light = choose(dict_intersections)

        aidans_table = progress(light, aidans_table)

if __name__ == '__main__':
    main()
