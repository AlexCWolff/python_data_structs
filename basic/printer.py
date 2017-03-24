"""TODO: decrease hardcoding and allow more args"""

import random
from queue import Queue

"""Simulates usage of a print queue, and output statistics if it is used on average 20 times per hour at certain ppm."""


class Printer:
    def __init__(self, ppm):
        self.pagerate = ppm
        self.current_task = None
        self.time_remaining = 0

    def tick(self):
        if self.current_task is not None:
            self.time_remaining -= 1
            if self.time_remaining <= 0:
                self.current_task = None

    def busy(self):
        if self.current_task is not None:
            return True
        else:
            return False

    def start_next(self, newtask):
        self.current_task = newtask
        self.time_remaining = newtask.get_pages() * 60 / self.pagerate


class Task:
    def __init__(self, time):
        self.timestamp = time
        self.pages = random.randrange(1, 21)

    def get_stamp(self):
        return self.timestamp

    def get_pages(self):
        return self.pages

    def wait_time(self, current_time):
        return current_time - self.timestamp


def simulation(num_seconds, pages_per_minute):

    labprinter = Printer(pages_per_minute)
    print_queue = Queue()
    waitingtimes = []

    for current_second in range(num_seconds):

        if new_print_task():
            task = Task(current_second)
            print_queue.enqueue(task)

        if (not labprinter.busy()) and (not print_queue.is_empty()):
            next_task = print_queue.dequeue()
            waitingtimes.append(next_task.wait_time(current_second))
            labprinter.start_next(next_task)

        labprinter.tick()

    average_wait = sum(waitingtimes) / len(waitingtimes)
    print("Average Wait %6.2f secs %3d tasks remaining."%(average_wait, print_queue.size()))


def new_print_task():
    num = random.randrange(1, 181)
    if num == 180:
        return True
    else:
        return False

print("10 print jobs, 5ppm")
for i in range(10):
    simulation(3600, 5)

print("10 print jobs, 10ppm")
for i in range(10):
    simulation(3600, 10)
