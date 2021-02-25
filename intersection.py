from collections import defaultdict

def intersection(lst):
    inter = defaultdict(int)
    for _, position in lst:
        if position is not None:
            inter[position] += 1
    
    return dict(inter)