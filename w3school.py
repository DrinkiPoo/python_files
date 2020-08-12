import numpy as np
from functions import mm, mp, pm, pp
import math
import openpyxl

def myfunc(x):
    y = x
    max_value = pp(x, y)
    max_possible_set = np.array([])
    raw_data = np.array([])

    for r in range(1, x + 1):
        max_possible_for_each_digit = math.floor((max_value + r) / (6 * r - 1))
        max_possible_set = np.append(max_possible_set, max_possible_for_each_digit)

    for r in range(1, x + 1):
        for s in range(1, int(max_possible_set[r - 1]) + 1):
            raw_data = np.append(raw_data, mm(r, s))
            raw_data = np.append(raw_data, mp(r, s))
            raw_data = np.append(raw_data, pm(r, s))
            raw_data = np.append(raw_data, pp(r, s))

    raw_data.sort()
    tapered = raw_data[:np.where(raw_data == max_value)[0][0] + 1]

    final = np.array([])
    final_one = np.array([])

    for r in tapered:
        if r not in final:
            final = np.append(final, r)


    for r in range(1, max_value + 1):
        if r not in final:
            final_one = np.append(final_one, r)


    primes = [(3, 5)]
    q = 1
    for r in final_one:
        primes.append((6 * int(r) - 1, 6 * int(r) + 1))
        q += 1

    print(primes)
    return x, q + 1

arr = []
for x in range(1, 10):
    arr.append(myfunc(x))

print(arr)