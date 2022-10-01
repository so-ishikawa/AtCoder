
N, Q = map(int, input().split())

L = []
for i in range(N):
    L.append([int(i) for i in input().split()])

ts = [list(map(int, input().split())) for l in range(Q)]


for i in ts:
    t = i[0]
    s = i[1]
    print(L[t-1][s])

