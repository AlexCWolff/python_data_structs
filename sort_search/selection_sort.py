"""
Selection sort is an improved version of bubble sort. Every pass it swaps the next largest item to it's correct place.
While it has the same worst case time as bubble it has much better averages, and is just as simple. 
NOTE: It does not insert, it swaps.
"""


def selection_sort(alist):
    for fill_slot in range(len(alist) - 1, 0, -1):
        position_of_max = 0
        for location in range(1, fill_slot + 1):
            if alist[location] > alist[position_of_max]:
                position_of_max = location

        temp = alist[fill_slot]
        alist[fill_slot] = alist[position_of_max]
        alist[position_of_max] = temp


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
selection_sort(alist)
print(alist)

