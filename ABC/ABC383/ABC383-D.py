

import math

N = int(input())


def get_prime(num):
    if num < 2:
        return([])

    temp = [True] * (num + 1)
    temp[0] = temp[1] = False
    for i in range(2, int(math.sqrt(num)) + 1):
        if temp[i]:
            for j in range(i * i, num + 1, i):
                temp[j] = False
    return [x for x in range(len(temp)) if temp[x]]

temp = get_prime(int(math.sqrt(N)))

count = 0
for i in range(len(temp)-1):
    for j in range(i+1, len(temp)):
        if int(math.sqrt(N)) < temp[i]*temp[j]:
            break
        count += 1

count_ = 0
for i in temp:
    if N < i**8:
        break
    count_ += 1

print(count+count_)

"""
import math

N = int(input())

def get_prime(num):
    temp = [True] * (num + 1)
    temp[0] = temp[1] = False
    for i in range(2, int(math.sqrt(num)) + 1):
        if temp[i]:
            for j in range(i * i, num + 1, i):
                temp[j] = False
    return [x for x in range(len(temp)) if temp[x]]

primes = get_prime(int(math.sqrt(N)))

count = 0

# Count p^8
for p in primes:
    if p**8 <= N:
        count += 1

count_ = 0
# Count p^2 * q^2
for i in range(len(primes)):
    for j in range(i + 1, len(primes)):
        if primes[i]**2 * primes[j]**2 <= N:
            count_ += 1
        else:
            break

print(count , count_)
"""
