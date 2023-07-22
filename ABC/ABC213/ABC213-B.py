N = int(input())
A_list = list(map(int, input().split()))

A_list_copy = A_list.copy()
A_list_copy.sort()
booby_value = A_list_copy[-2]

print(A_list.index(booby_value)+1)
