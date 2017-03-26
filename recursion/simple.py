"""
This was really tricky, I had to get help. Don't feel bad if you are confused.
"""


def list_sum(num_list):
    """A very basic recursive algorithm. Adds each number in a list individually until there is only one left."""
    if len(num_list) == 1:
        # This is the base case, if the list only has one item recursion stops.
        # Recursion does not stop until this base condition is met.
        return num_list[0]
    else:
        # The algorithm changes its state, moves towards the base case,
        # then calls itself again until the base condition it met.
        return num_list[0] + list_sum(num_list[1:])

assert list_sum([1, 3, 5, 7, 9]) is 25


def to_str(n, base):
    """Converts a string to it's base representation by dividing it by the base and concatenating the remainders."""
    convert_string = "0123456789ABCDEF"
    if n < base:
        return convert_string[n]
    else:
        return to_str(n // base, base) + convert_string[n % base]

assert to_str(1453, 16) == "5AD"


def reverse(s):
    """Reverses a string recursively."""
    if len(s) <= 1:
        return s[0]
    else:
        # Keep slicing off all remaining characters until there is only one left,
        # then the functions return each character in reverse order as their base conditions are met.
        return reverse(s[1:]) + s[0]

assert reverse("hello") == "olleh"


def clean_string(s):
    """Cleans a string of everything but alphanumeric characters."""
    return ''.join(e for e in s if e.isalnum())


def is_palindrome(s):
    """Recursively checks is a string is a palindrome."""
    s = clean_string(s)
    if len(s) <= 1:
        return True
    else:
        return s[0] == s[-1] and is_palindrome(s[1:-1])

assert is_palindrome("kayak") is True
assert is_palindrome("follow") is False
assert is_palindrome("madam i'm adam") is True

