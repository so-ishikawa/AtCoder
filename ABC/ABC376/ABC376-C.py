N = int(input())
A_list = list(map(int, input().split()))
B_list = list(map(int, input().split()))

A_list.sort(reverse=True)
B_list.sort(reverse=True)

box_size = 0
for i in range(len(A_list)):
    if i == len(A_list)-1:
        print(A_list[i])
        exit()
    if A_list[i] <= B_list[i]:
        continue
    box_size = A_list[i]
    break

B_list.append(box_size)
B_list.sort(reverse=True)

for i in range(len(A_list)):
    if A_list[i] <= B_list[i]:
        continue
    print(-1)
    exit()

print(box_size)
