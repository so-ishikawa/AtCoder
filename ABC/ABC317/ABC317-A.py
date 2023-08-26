N, H, X = map(int, input().split())
P_list = []
P_list = list(map(int, input().split()))
for i in range(N):
    p = P_list[i]
    if X <= p + H:
        print(i+1)
        exit()

