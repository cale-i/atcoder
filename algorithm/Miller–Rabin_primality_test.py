"""
【ミラー–ラビン素数判定法】
"""

import random
from math import gcd
import os


def is_prime(n):
    if n == 2:
        return True
    if n == 1:
        return False
    # 2を超える偶数
    if n % 2 == 0:
        return False

    # n-1を右シフト(2で除す)
    d = (n - 1)
    while d % 2 == 0:
        d //= 2

    randint = get_randint(int(n))

    for a in randint:
        t = d
        y = pow(a, t, n)

        while t != n - 1 and y != 1 and y != n - 1:
            y = (y * y) % n
            t *= 2

        if y != n - 1 and t % 2 == 0:
            return False

    return True


def get_randint(n):
    test_num = set()
    TRIAL_NUM = 100
    while len(test_num) < TRIAL_NUM:
        a = random.randint(2, n - 1)
        if a in test_num:
            continue
        test_num.add(a)

    return test_num


mersenne_number = 2 ** 89 - 1
carmichael_number = 1729


# n = 561
# n = mersenne_number
n = carmichael_number
# n = 5998697994190188741057

print(is_prime(int(n)))
