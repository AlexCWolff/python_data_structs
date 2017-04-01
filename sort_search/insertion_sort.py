"""
Insertion sort again has the same complexity as bubble and selection, but even better performance.
Insertion works from the front and inserts rather than swaps, using 1/3 of the processing power.
"""


def insertion_sort(alist):
    for index in range(1, len(alist)):
        current_value = alist[index]
        position = index

        while position > 0 and alist[position - 1] > current_value:
            alist[position] = alist[position - 1]
            position -= 1

        alist[position] = current_value


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
insertion_sort(alist)
print(alist)
