"""
A binary heap is a type of priority queue, where the logical order of items inside is determined by their 
priority, therefore items can be enqueued or dequeued at O(log n). While it is a tree, in practice it looks like an 
ordered list. 
"""


class BinHeap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    def perc_up(self, i):
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i // 2]:
                tmp = self.heapList[i // 2]
                self.heapList[i // 2] = self.heapList[i]
                self.heapList[i] = tmp
            i = i // 2

    def perc_down(self, i):
        while (i * 2) <= self.currentSize:
            mc = self.min_child(i)
            if self.heapList[i] > self.heapList[mc]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp
            i = mc

    def min_child(self, i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i * 2] < self.heapList[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def insert(self, k):
        self.heapList.append(k)
        self.currentSize = self.currentSize + 1
        self.perc_up(self.currentSize)

    def del_min(self):
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heapList.pop()
        self.perc_down(1)
        return retval

    def build_heap(self, alist):
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        while i > 0:
            self.perc_down(i)
            i = i - 1

if __name__ == "__main__":
    bh = BinHeap()
    bh.build_heap([9, 5, 6, 2, 3])

    print(bh.del_min())
    print(bh.del_min())
    print(bh.del_min())
    print(bh.del_min())
    print(bh.del_min())