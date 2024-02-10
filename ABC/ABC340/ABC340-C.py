import math
import sys
sys.setrecursionlimit(99999999)

N = int(input())

dic = dict()

def f(n):
    if n < 2:
        return(0)
    if n in dic:
        return(dic[n])
    temp0 = f(n//2)
    temp1 = f(math.ceil(n/2))
    result = temp0 + temp1 + n
    if result not in dic:
        dic[n] = result
    return(result)

print(f(N))
