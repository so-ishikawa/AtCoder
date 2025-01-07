import math
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

X = int(input())

primes_list = get_prime(2*X)
print(min([x for x in primes_list if x>=X] ))
