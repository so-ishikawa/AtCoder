N = int(input())
A_list = list(map(int, input().split()))
_A_list = A_list.copy()
_A_list.sort()

print(A_list.index(_A_list[-2])+1)

