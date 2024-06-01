N, L, R = map(int, input().split())
temp = list(range(1, N+1))
hoge = temp[L-1:R]
pre = temp[:L-1]
aft = temp[R:]
hoge.reverse()
print(*pre, *hoge, *aft)
