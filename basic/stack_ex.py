from stack import Stack, ReverseStack

STACK = Stack()
REVERSE_STACK = ReverseStack()

print(STACK.is_empty())
STACK.push(4)
STACK.push('dog')
print(STACK.peek())
STACK.push(True)
print(STACK.size())
print(STACK.is_empty())
STACK.push(8.4)
print(STACK.pop())
print(STACK.pop())
print(STACK.size())

REVERSE_STACK.push('hello')
REVERSE_STACK.push('true')
print(REVERSE_STACK.pop())


def par_checker(symbol_string):
    """
    Uses a stack to ensure that all parentheses and brackets in a string
    have a closing paran/bracket of the same type in the right place.
    """
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbol_string) and balanced:
        symbol = symbol_string[index]
        if symbol in "([{":
            s.push(symbol)
        else:
            if s.is_empty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top, symbol):
                    balanced = False
        index += 1
    if balanced and s.is_empty():
        return True
    else:
        return False

def matches(open, close):
    """Handle bracket/paran matching."""
    openers = "([{"
    closers = ")]}"
    return openers.index(open) == closers.index(close)


print(par_checker('{{([][])}()}'))
print(par_checker('[{()]'))


def base_converter(number, base):
    """Converts decimal numbers to any base numbering system up to base 36."""
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    remstack = Stack()

    while number > 0:
        rem = number % base
        remstack.push(rem)
        number = number // base

    new_string = ""
    while not remstack.is_empty():
        new_string = new_string + digits[remstack.pop()]

    return new_string

print(base_converter(25, 2))
print(base_converter(25, 16))
print(base_converter(26, 26))
