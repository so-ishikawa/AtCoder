N = int(input())
A_list = list(map(int, input().split()))

temp = sum(A_list)
if temp == 0:
    print(0)
    exit()

print(-1*temp)
