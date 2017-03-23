"""
TODO: Add log linear, cubic, exponential, more timers, examples
"""


def constant(n):
    """aka O(1), this is the ideal. Just one operation."""
    return n


def logarithmic(n):
    """aka O(log n)"""
    i = n
    while i > 0:
        i //= 2
    return i


def linear(n):
    """aka O(n). One operation every iteration."""
    m = 0
    for i in n:
       m += i
    return m


def quadratic(n):
    """aka O(n^2). Nested iterations with one operation for every nested iteration."""
    m = 0
    for i in n:
        for j in n:
            m += j
    return m

if __name__ == '__main__':
    import timeit
    T1 = timeit.timeit(lambda: constant(5), number=10000)
    T2 = timeit.timeit(lambda: logarithmic(5), number=10000)
    T3 = timeit.timeit(lambda: linear([1, 2, 3, 4, 5]), number=10000)
    T4 = timeit.timeit(lambda: quadratic([1, 2, 3, 4, 5]), number=10000)

    print(T1)
    print(T2)
    print(T3)
    print(T4)
