N = int(input())
A_list = list(map(int, input().split()))
A_list.sort()
count = 1
# print(A_list)
for i in range(3, len(A_list), 4):
    # print(count, A_list[i])
    if count != A_list[i]:
        print(count)
        exit()
    count += 1

print(count)
exit()
