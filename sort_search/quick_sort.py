"""
Quick sort tries to balance the benefits of merge sort with lower memory usage, but can sometimes end up O(n^2) 
when a poor pivot value is chosen. It first selects a pivot value to help it split the list, and then moves (
partitions) all other items higher or lower to their respective sides of this, starting from the end on both sides 
and moving in towards the pivot. Only one outside marker moves at a time, and when it finds an item that belongs on 
the other side, it is inserted by the other marker, which then moves. When the marker starting from the end becomes 
smaller than the marker starting from the beginning, it stops and this becomes the new split point where the pivot 
value is inserted. The list is then divided at the split point and quick sort is called recursively on the two 
halves (as one list, not two; and on the left half first). 
http://interactivepython.org/runestone/static/pythonds/_images/firstsplit.png 
http://interactivepython.org/runestone/static/pythonds/_images/partitionA.png 
http://interactivepython.org/runestone/static/pythonds/_images/partitionB.png 

TODO: Median of three (first, middle. last) pivot value.
"""


def quick_sort(alist):
    quick_sort_helper(alist, 0, len(alist) - 1)


def quick_sort_helper(alist, first, last):
    if first < last:
        split_point = partition(alist, first, last)

        quick_sort_helper(alist, first, split_point - 1)
        quick_sort_helper(alist, split_point + 1, last)


def partition(alist, first, last):
    pivot_value = alist[first]

    left_mark = first + 1
    right_mark = last

    done = False
    while not done:

        while left_mark <= right_mark and alist[left_mark] <= pivot_value:
            left_mark = left_mark + 1

        while alist[right_mark] >= pivot_value and right_mark >= left_mark:
            right_mark = right_mark - 1

        if right_mark < left_mark:
            done = True
        else:
            temp = alist[left_mark]
            alist[left_mark] = alist[right_mark]
            alist[right_mark] = temp

    temp = alist[first]
    alist[first] = alist[right_mark]
    alist[right_mark] = temp

    return right_mark


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
quick_sort(alist)
print(alist)
