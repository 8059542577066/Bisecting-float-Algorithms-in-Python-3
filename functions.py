def golden():
    x, m = 1, 1 / 2
    while x + m != x - m:
        if x ** 2 - x - 1 < 0:
            x += m
        else:
            x -= m
        m /= 2
    return x

def plastic():
    x, m = 1, 1 / 2
    while x + m != x - m:
        if x ** 3 - x - 1 < 0:
            x += m
        else:
            x -= m
        m /= 2
    return x

def pentagon():
    x, m = 1, 1 / 2
    while x + m != x - m:
        if 256 * x ** 4 - 800 * x ** 2 + 125 < 0:
            x += m
        else:
            x -= m
        m /= 2
    return x

def hexagon():
    x, m = 2, 1 / 2
    while x + m != x - m:
        if 4 * x ** 2 - 27 < 0:
            x += m
        else:
            x -= m
        m /= 2
    return x

def sqrt(n):
    x = 1
    while x ** 2 < n:
        x *= 2
    m = x / 2
    while x + m != x - m:
        if x ** 2 < n:
            x += m
        else:
            x -= m
        m /= 2
    return x

def cbrt(n):
    x = 1
    while x ** 3 < n:
        x *= 2
    m = x / 2
    while x + m != x - m:
        if x ** 3 < n:
            x += m
        else:
            x -= m
        m /= 2
    return x
