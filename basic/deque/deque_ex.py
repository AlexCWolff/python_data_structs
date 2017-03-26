from deque import Deque

d = Deque()

"""
Test the methods of our deque. This could be accomplished with print statements as with 
the stack and queue, but why do that when python can do it for us more accurately?
"""
assert d.is_empty() is True
d.add_rear(4)
d.add_rear('dog')
d.add_front('cat')
d.add_front(True)
assert d.size() is 4
assert d.is_empty() is False
d.add_rear(8.4)
assert d.remove_rear() is 8.4
assert d.remove_front() is True


def palindrome_checker(s):
    # Check if a passed string is a palindrome, i.e. the same forwards as backwards.
    # Create a new deque object for us to use.
    char_deque = Deque()

    # For every character in the string
    for ch in s:
        # Add it to the rear of the deque
        char_deque.add_rear(ch)

    # A boolean to help us track if the characters are still matching.
    still_equal = True

    """ 
    While there is more than one character in the deque and the characters are still matching. 
    If there is only one character left, it's exactly in the middle and will always be the same.
    """
    while char_deque.size() > 1 and still_equal:
        # Grab the next items from the front and rear of the deque
        first = char_deque.remove_front()
        last = char_deque.remove_rear()
        # If these two characters are not the same it's not a palindrome, so we change the boolean.
        if first != last:
            still_equal = False

    # Return the boolean
    return still_equal

print(palindrome_checker("lsdkjfskf"))
print(palindrome_checker("radar"))
