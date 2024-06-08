N = int(input())
keta = len(str(N))
r = 10**keta
m = 998244353
sum_ = 0
for i in range(N):
    sum_ = (sum_ + (N * r**i)) % m

print(sum_)
