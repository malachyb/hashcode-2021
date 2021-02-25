#!/usr/bin/env python3

from take_input import take_input
from street_input import street_input
from make_table import make_table
from intersection import intersection
from choose_light import choose

def main():
    file = input()
    duration, intersections, streets, cars, bonus = take_input(file)

    list_intersections, dict_streets, list_cars = street_input(file, intersections, streets, cars)

    aidans_table = make_table(list_cars, dict_streets, duration)

    dict_intersections = intersection(aidans_table[0])

if __name__ == '__main__':
    main()
