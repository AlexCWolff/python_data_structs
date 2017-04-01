"""
This is the simplest sorting algorithm, and also the slowest. You shouldn't ever use it.
The only exception to this rule is if a list is already sorted, it will notice faster.
"""


def bubble_sort(alist):
    # I forget all the time range can take 3 args: start, stop, and step.
    for pass_num in range(len(alist) - 1, 0, -1):
        for i in range(pass_num):
            if alist[i] > alist[i + 1]:
                temp = alist[i]
                alist[i] = alist[i + 1]
                alist[i + 1] = temp


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
bubble_sort(alist)
print(alist)


def short_bubble_sort(alist):
    # Seems kludge-y, probably a better way.
    exchanges = True
    pass_num = len(alist) - 1
    while pass_num > 0 and exchanges:
        exchanges = False
        for i in range(pass_num):
            if alist[i] > alist[i + 1]:
                exchanges = True
                temp = alist[i]
                alist[i] = alist[i + 1]
                alist[i + 1] = temp
        pass_num = pass_num - 1


alist = [20, 30, 40, 90, 50, 60, 70, 80, 100, 110]
short_bubble_sort(alist)
print(alist)
