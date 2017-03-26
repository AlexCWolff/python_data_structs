"""
TODO: Explain
"""


def move_tower(height, from_pole, to_pole, with_pole):
    # We don't need to use stacks to track the disks, python does this implicitly for us with the call stack.
    if height >= 1:
        move_tower(height - 1, from_pole, with_pole, to_pole)
        move_disk(from_pole, to_pole)
        move_tower(height - 1, with_pole, to_pole, from_pole)


def move_disk(fp, tp):
    print("moving disk from pole", fp, "to pole", tp)

move_tower(3, "A", "B", "C")
