N, K = map(int, input().split())
A_list = list(map(int, input().split()))

temp = [x//K for x in A_list if x % K == 0]
temp.sort()
for i in temp:
    print(i, end=" ")
