"""
Merge sort is more advanced, it's a recursive sorting algorithm. The base case is there only being one item, 
which means it is inherently sorted. As the items are returned and combined, they are inserted appropriately.
It starts from the beginning, working its way down before working towards the end.
An image makes this process very easy to understand:
http://interactivepython.org/runestone/static/pythonds/_images/mergesortA.png
A merge sort is an O(n log n) algorithm but uses extra memory, creating problems with large datasets.

TODO: Remove slice, pass the starting and ending indices along with the list making the recursive call
"""


def merge_sort(alist):
    print("Splitting ", alist)
    if len(alist) > 1:
        mid = len(alist) // 2
        left_half = alist[:mid]
        right_half = alist[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = 0
        j = 0
        k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                alist[k] = left_half[i]
                i = i + 1
            else:
                alist[k] = right_half[j]
                j = j + 1
            k = k + 1

        while i < len(left_half):
            alist[k] = left_half[i]
            i = i + 1
            k = k + 1

        while j < len(right_half):
            alist[k] = right_half[j]
            j = j + 1
            k = k + 1
    print("Merging ", alist)


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
merge_sort(alist)
print(alist)
