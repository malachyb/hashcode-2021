from collections import defaultdict
import sys


def choose(dict):
    street = max(dict.items())
    street = street[0]
    return street
    
if __name__ == '__main__':
    dict = {"street_1":1, "street_2": 3}
    choose(dict)