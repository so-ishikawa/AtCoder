import math

# k = int(input())


def prime_factorization(num):
    """
    素因数分解
    list型で(素因数, 指数)を返す
    """
    result = []
    prime_number = 2
    temp = num

    while prime_number**2 <= num:
        e = 0
        while temp % prime_number == 0:
            temp //= prime_number
            e += 1
        if e > 0:
            result.append((prime_number, e))
        prime_number += 1
    if temp > 1:
        result.append((temp, 1))
    return result


def legendre(n, p):
    """
    n! を pで何回割り切れるか
    """
    _p = p
    sum_ = 0
    while True:
        temp = n / _p

        if temp < 1:
            break
        sum_ += temp
        _p = _p * p
    return int(sum_)

print(legendre(30,3))
