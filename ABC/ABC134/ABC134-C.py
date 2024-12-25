N = int(input())
A_list = []

for i in range(N):
    temp = int(input())
    A_list.append(temp)

B_list = A_list.copy()

A_list.sort(reverse=True)

for b in B_list:
    if b == A_list[0]:
        print(A_list[1])
        continue
    print(A_list[0])


