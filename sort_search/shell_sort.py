"""
Shell short is kind of weird to wrap your head around, because it is an improvement on insertion sort 
while seemingly doing more work. It works by breaking down the list in to sub lists by an increment, 
so if an increment of 3 is given for nine items, every third item is added to one of 3 sub-lists 
based on their position. These sub-lists are then insertion sorted, then each item is inserted back in order.
For example, 4 items with an increment of 2: 
[3, 1, 2, 4]
Becomes:
[3, 2] and [1, 4]
Sorted:
[2, 3] and [1, 4]
Re-inserted in the new order:
[2, 1, 3, 4]
Then a final insertion sort is run. This way tends to cut down on the number of insertions and get closer to O(n).
"""


def shell_sort(alist):
    sublist_count = len(alist) // 2
    while sublist_count > 0:
        for start_position in range(sublist_count):
            gap_insertion_sort(alist, start_position, sublist_count)

        print("After increments of size", sublist_count, "The list is", alist)

        sublist_count //= 2


def gap_insertion_sort(alist, start, gap):
    for i in range(start + gap, len(alist), gap):

        current_value = alist[i]
        position = i

        while position >= gap and alist[position - gap] > current_value:
            alist[position] = alist[position - gap]
            position -= gap

        alist[position] = current_value


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
shell_sort(alist)
print(alist)
