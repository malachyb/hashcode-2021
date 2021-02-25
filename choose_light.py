from collections import defaultdict
import sys


def choose(dict):
    street = max(dict.items())
    return (street[0])
    
if __name__ == '__main__':
    dict = {"street_1":1, "street_2": 3}
    choose(dict)