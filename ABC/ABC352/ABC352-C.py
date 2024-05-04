N = int(input())
A_list = []
B_list = []

max_diff = 0
max_index = -1

for index in range(N):
    A, B = map(int, input().split())
    A_list.append(A)
    B_list.append(B)

    temp = B - A
    if temp > max_diff:
        max_diff = temp
        max_index = index


print(sum(A_list) - A_list[max_index] + B_list[max_index])
