L, H = map(int, input().split())
N = int(input())
A_list = []
for _ in range(N):
    A_list.append(int(input()))

for i in A_list:
    if i < L:
        print(L-i)
        continue
    if L <= i and i <= H:
        print(0)
        continue
    if H < i:
        print(-1)
        continue

