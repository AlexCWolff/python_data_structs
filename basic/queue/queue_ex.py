from queue import Queue


def hot_potato(namelist, num):
    """Determines who is holding the potato when the counter hits 0."""
    # Creates a queue
    simqueue = Queue()
    # Loops through the names, putting them in the queue
    for name in namelist:
        simqueue.enqueue(name)

    # While the queue has more than 1 person left.
    while simqueue.size() > 1:
        # For every number in the range given, take the next person from the front and place them in the back
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())

        # Take the person from the front
        simqueue.dequeue()

    # Return the person from the front.
    return simqueue.dequeue()

print(hot_potato(["Bill", "David", "Susan", "Jane", "Kent", "Brad"], 7))
