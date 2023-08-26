N = int(input())
A_list = list(map(int, input().split()))

A_list.sort()

for i in range(len(A_list)-1):
    if A_list[i+1] - A_list[i] != 1:
        print(A_list[i]+1)
        exit()
