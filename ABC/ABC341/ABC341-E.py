from math import log2, ceil

def invert_bitwise(x):
    if x == 0:
        d = 1
    else:
        d = ceil(log2(abs(x))) + 1
    mask = (1 << d) - 1
    tmp = ~x
    orig_repr = f'{x & mask:0= {d+1}b}'
    inverted_repr = f'{tmp & mask:0= {d+1}b}'
    #print(f'{orig_repr}\n{inverted_repr}')
    return orig_repr, inverted_repr

N, Q = map(int, input().split())
S = int(input())
"""
for _ in range(Q):
    num, L, R = map(int, input().split())
"""
print(invert_bitwise(20))
