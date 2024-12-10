import math
N = int(input())
q_dic = dict()

for i in range(1, N+1):
    q, r = map(int, input().split())
    q_dic[i] = (q, r)

Q = int(input())
for _ in range(Q):
    t, d = map(int, input().split())
    q, r = q_dic[t]

    if r >= d:
        print(r)
        continue

    x = math.ceil((d - r) / q)
    print(q*x+r)
