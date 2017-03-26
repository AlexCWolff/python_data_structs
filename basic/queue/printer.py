import random
from queue import Queue

"""
Simulates usage of a lab printer, and outputs statistics for printer usage with given configurations.
"""


class Printer:
    """
    Class to simulate our lab printer.
    Takes page rate as input.
    Returns if the printer is busy or not.
    Contains methods for changing the time remaining on the current task and starting the next task. 
    """
    def __init__(self, ppm):
        # Initializes our printer with the given ppm rate, sets the queue to empty.
        self.page_rate = ppm
        self.current_task = None
        self.time_remaining = 0

    def tick(self):
        """Every second (tick), if there is a current task"""
        if self.current_task is not None:
            # Take one second off the time remaining
            self.time_remaining -= 1
            # If time remaining is zero or less
            if self.time_remaining <= 0:
                # Remove the task.
                self.current_task = None

    @property
    def busy(self):
        """
        Determine if the printer is currently busy. Since this performs no actions,
        this is just a property of the Printer class, not a method.
        """
        if self.current_task is not None:
            return True
        else:
            return False

    def start_next(self, new_task):
        """Add a new task to the printer."""
        self.current_task = new_task
        # Set the time remaining to the number of pages, times 60, divided by ppm
        self.time_remaining = new_task.get_pages * 60 / self.page_rate


class Task:
    """ 
    Class to simulate our task. 
    Takes the time the task was submitted and page count as input.
    Returns the timestamp, page count, and wait time as output.
    """
    def __init__(self, time, pages):
        """Initialize our task with the time it was submitted and the page count."""
        self.timestamp = time
        self.pages = random.randrange(1, pages+1)

    @property
    def get_stamp(self):
        """Get the timestamp for the task"""
        return self.timestamp

    @property
    def get_pages(self):
        """Get the page count for the task."""
        return self.pages

    def wait_time(self, current_time):
        """Get the wait time for the task"""
        return current_time - self.timestamp


def simulation(num_seconds, ppm, page_limit, student_avg, job_avg):
    """
    This function handle our simulation of the printer and it's usage. 
    Takes the number of seconds you want to run the simulation for, page rate of the printer, 
        the max page count, the student average per the time limit, and the average number of jobs per student.
    Prints the average wait time of students and how many tasks are remaining. 
    """
    # Create our lab printer and set the ppm
    lab_printer = Printer(ppm)
    # Create our print queue
    print_queue = Queue()
    # Create a list to hold our wait times to be averaged
    waiting_times = []

    # For every second in the number of seconds provided (aka, every tick)
    for current_second in range(num_seconds):
        # If there is a new print task
        if new_print_task(num_seconds, student_avg, job_avg):
            # Create a task and give it the current time and page limit
            task = Task(current_second, page_limit)
            # Queue it up in the printer
            print_queue.enqueue(task)

        # If the lab printer is not busy and the print queue is not empty
        if (not lab_printer.busy) and (not print_queue.is_empty()):
            # Dequeue the next task
            next_task = print_queue.dequeue()
            # Add to its waiting time
            waiting_times.append(next_task.wait_time(current_second))
            # Start the task
            lab_printer.start_next(next_task)

        # Add one tick to the printer
        lab_printer.tick()

    # Average out the waiting time for every task
    average_wait = sum(waiting_times) / len(waiting_times)
    print("Average Wait %6.2f secs %3d tasks remaining." % (average_wait, print_queue.size()))


def new_print_task(seconds, students, jobs):
    """Randomly determine if there should be a new task or not, based on given variables."""
    time_in_hours = seconds / 60 / 60
    # Get the number of tasks per hour
    tasks_per_hour = students * jobs / time_in_hours
    # Set up the chance of a new task running every second
    num = random.randrange(1, tasks_per_hour+1)
    # Return true if it's time for a new job
    if num == tasks_per_hour:
        return True
    else:
        return False

print("\n1 hour, 5ppm, 20 page limit, 20 student average, 2 jobs per student")
print("-------------------------------------------------------------------")
for i in range(10):
    simulation(3600, 5, 20, 20, 2)

print("\n1 hour, 10ppm, 30 page limit, 30 student average, 5 jobs per student")
print("-------------------------------------------------------------------")
for i in range(10):
    simulation(3600, 10, 30, 30, 5)

print("\n1 hour, 20ppm, 20 page limit, 50 student average, 2 jobs per student")
print("-------------------------------------------------------------------")
for i in range(10):
    simulation(3600, 20, 20, 50, 2)
