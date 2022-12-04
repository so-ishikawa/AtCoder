import math

k = int(input())


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

    _p = p
    sum_ = 0
    while True:
        temp = n // _p

        if temp == 0:
            break
        sum_ += temp
        _p = _p * p
    return int(sum_)

"""
# n! は p で何回割り切れるか（ルジャンドルの定理）
def legendre(n, p):
  res = 0
  p2 = p
  while True:
    tmp = n // p2
    if tmp == 0:
      break
    res += tmp
    p2 *= p
  return res
"""

 
prime_list = prime_factorization(k)
max_prime = prime_list[len(prime_list)-1][0]
# print(max_prime, prime_list)

# 判定問題
def isok(n, pes):
  for p, e in pes:
    if legendre(n, p) < e:
      return False
  return True

# 二分探索
ng, ok = 1, k  # k ≥ 2 なので 1! は k の倍数にならない、また k! は必ず k の倍数
while abs(ok - ng) > 1:
  mid = (ok + ng) // 2
  if isok(mid, prime_list):
    ok = mid
  else:
    ng = mid
print(ok)
