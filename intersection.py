from collections import defaultdict

def intersection(lst):
    inter = defaultdict(int)
    for position in lst:
        inter[position] += 1
    
    return dict(inter)