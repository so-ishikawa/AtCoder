N, M = map(int, input().split())
A_list = list(map(int, input().split()))

A_list.sort(reverse=True)

if A_list[M-1]*(4*M) >= sum(A_list):
    print("Yes")
    exit()
print("No")
