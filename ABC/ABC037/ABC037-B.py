N, Q = map(int, input().split())
a_list = [0]*N
for _ in range(Q):
    l, r, t = map(int, input().split())
    for i in range(l-1, r-1+1):
        a_list[i] = t

for i in range(len(a_list)):
    print(a_list[i])
