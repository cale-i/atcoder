# 素数定理

import math


def get_num(x):
    return x / (math.log(x, math.e))


# x = 10**216
# print(get_num(10**216) - get_num(10**215))

# print(get_num(10**215))
