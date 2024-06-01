N, M = map(int, input().split())

N = N %  998244353
M = M %  998244353

sum_ = 0
for k in range(N+1):
    temp = k & M
    """
    a = bin(temp)[2:].count("1")
    while a > 998244353:
        a = a - 998244353
    sum_ += a
    """
print(sum_)
