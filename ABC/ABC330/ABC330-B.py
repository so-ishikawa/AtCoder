N, L, R = map(int, input().split())
A_list = list(map(int, input().split()))

for i in A_list:
    if L <= i and i <= R:
        print(i, end=" ")
        continue
    if i < L:
        print(L, end=" ")
        continue
    if R < i:
        print(R, end=" ")
        continue

