__version__ = "0.1.0"


def fibonacci(n):
    return sum_series(n)


def lucas(n):
    return sum_series(n, 2, 1)


def sum_series(n, x=0, y=1):
    if n >= 0:
        if n == 0:
            return x
        if n == 1:
            return y
        if n > 1:
            return sum_series(n - 1, x, y) + sum_series(n - 2, x, y)
    else:
        return "wrong input"
