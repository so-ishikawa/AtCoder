N = int(input())
T_list = list(map(int, input().split()))
M = int(input())
for i in range(M):
    p, x = map(int, input().split())
    temp = sum(T_list) - T_list[p-1] + x
    print(temp)
