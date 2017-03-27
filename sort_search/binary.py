"""
TODO: Clean code, explain
"""

def binary_search_simple(alist, item):
    first = 0
    last = len(alist)-1

    while first <= last:
        midpoint = (first + last) // 2
        if alist[midpoint] == item:
            return True
        else:
            if item < alist[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1

    return False

testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print(binary_search_simple(testlist, 3))
print(binary_search_simple(testlist, 13))


def binary_search_recursive(alist, item):
    if len(alist) == 0:
        return False
    else:
        midpoint = len(alist) // 2
        if alist[midpoint] == item:
            return True
        else:
            if item < alist[midpoint]:
                return binary_search_recursive(alist[:midpoint], item)
            else:
                return binary_search_recursive(alist[midpoint + 1:], item)

testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print(binary_search_recursive(testlist, 3))
print(binary_search_recursive(testlist, 13))
