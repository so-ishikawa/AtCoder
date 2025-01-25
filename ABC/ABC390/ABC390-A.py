A1, A2, A3, A4, A5 = map(int, input().split())

A_list = [A1,A2,A3,A4,A5]
temp = [1,2,3,4,5]

count = 0
non_index_list = []
for i in range(5):
    if A_list[i] == temp[i]:
        count += 1
    else:
        non_index_list.append(i)

if count != 3:
    print("No")
    exit()

if non_index_list[1] - non_index_list[0] != 1:
    print("No")
    exit()

print("Yes")
