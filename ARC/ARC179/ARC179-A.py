N, K = map(int, input().split())
A_list = list(map(int, input().split()))

F = sum(A_list)
if K > 0:
    print("Yes")
    A_list.sort()
    print(*A_list)
    exit()

if K <= 0 and F >= K:
    print("Yes")
    A_list.sort(reverse=True)
    print(*A_list)
    exit()

if K <= 0 and F < K:
    print("No")
