N = int(input())
A_list = list(set(map(int, input().split())))

A_list.sort()
print(A_list[-2])

