"""
【フェルマーの小定理】
pを素数とするとき、
pと互いに素な整数aに対して以下が成り立つ。

a ^ (p−1) ≡ 1 (mod p)
a ^ (n−1) ≡ 1 (mod n)
"""

import random
from math import gcd


def is_prime(n, a):
    if n == 1:
        return False
    if n == 2:
        return True

    # 互いに素でない場合
    if gcd(n, a) != 1:
        False

    # フェルマーテスト
    if pow(a, n - 1, n) != 1:
        return False

    return True


mersenne_number = 2 ** 89 - 1
carmichael_number = 1729

TRIAL_NUM = 100
test_num = set()

n = carmichael_number
# n = mersenne_number

while len(test_num) < TRIAL_NUM:
    a = random.randint(2, n - 1)
    if a in test_num:
        continue

    test_num.add(a)

ans = True

for a in test_num:
    ans &= is_prime(n, a)
print(f'Is {n} prime number?: {ans}')
