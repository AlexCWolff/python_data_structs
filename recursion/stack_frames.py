# This is a relative import, if you don't have the whole repo this will cause you issues.
# Consider doing 'pip install pythonds' then using from pythonds.basic.stack import Stack
from ..basic.stack import Stack

r_stack = Stack()


def to_str(n, base):
    """Rather than concatenating the result, we can push it on to a stack before making a recursive call."""
    convert_string = "0123456789ABCDEF"
    while n > 0:
        if n < base:
            r_stack.push(convert_string[n])
        else:
            r_stack.push(convert_string[n % base])
        n = n // base
    res = ""
    # Since everything is on the stack, we can pop it until it is empty to make our string.
    while not r_stack.is_empty():
        res += str(r_stack.pop())
    return res

print(to_str(1453, 16))
