A, B, K = map(int, input().split())

lower = set(range(A,min(B+1, A+K)))
upper = set(range(B, max(A-1, B-K),-1))

temp = list(lower | upper)
temp.sort()
for i in temp:
    print(i)
