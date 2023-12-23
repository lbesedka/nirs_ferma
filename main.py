import numpy as np
import math


def get_m(n):
    return math.isqrt(n)


def get_full_square(n):
    m = get_m(n)
    k = 1
    while not (np.sqrt(math.pow((m + k), 2) - n)).is_integer():
        k += 1
    return m, k


def ferma_factorization(n):
    m, k = get_full_square(n)
    y = m + k
    x = np.sqrt(math.pow(y, 2) - n)
    p = np.abs(x + y)
    q = np.abs(x - y)
    return p, q


def get_n(p, q):
    return p*q


if __name__ == '__main__':
    p = 13
    q = 7
    n = get_n(p, q)
    p, q = ferma_factorization(n)
    print(p)
    print(q)
