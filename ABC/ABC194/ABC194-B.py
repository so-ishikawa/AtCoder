N = int(input())
A_list = []
B_list = []

for _ in range(N):
    a, b = map(int, input().split())
    A_list.append(a)
    B_list.append(b)

A_list_copy = A_list.copy()
B_list_copy = B_list.copy()

A_list_copy.sort()
B_list_copy.sort()

if A_list.index(A_list_copy[0]) != B_list.index(B_list_copy[0]):
    print(max(A_list_copy[0], B_list_copy[0]))
    exit()

a1b1 = A_list_copy[0] + B_list_copy[0]
a1b2 = max(A_list_copy[0], B_list_copy[1])
a2b1 = max(A_list_copy[1], B_list_copy[0])
print(min(a1b1, a1b2, a2b1))
