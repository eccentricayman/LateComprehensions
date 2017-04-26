def union(a, b):
    union = [i for i in a] + [i for i in b if not i in a]
    return union

def intersection(a, b):
    intersection = [i for i in a if i in b]
    return intersection

def set_difference(a, b):
    difference = [i for i in a if i not in b]
    return difference

def symmetric_difference(a, b):
    union = union(a, b)
    intersection = intersection(a, b)
    difference = set_difference(u, i)
    return difference

def cartesian(a, b):
    cartesian = [(a[i], b[i]) for i in range(len(a))]
    cartesian = ([(a[i], b[len(a) - 1 - i]) for i in range(len(a))])
    return cartesian
