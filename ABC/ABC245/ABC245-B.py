N = int(input())
A_list = list(map(int, input().split()))

for i in range(N+1):
    if i not in A_list:
        print(i)
        exit()
