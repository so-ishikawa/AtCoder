N = int(input())
A_list = list(map(int, input().split()))

A_list.sort()
print(abs(A_list[0]-A_list[-1]))
