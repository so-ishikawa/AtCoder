N, M = map(int, input().split())
A_list = list(map(int, input().split()))

if N >= sum(A_list):
    print(N-sum(A_list))
    exit()
print(-1)
exit()
