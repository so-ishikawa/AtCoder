N = int(input())
a_list = list(map(int, input().split()))

pass_flag = False
counter = 0

a_list.sort()
for i in range(len(a_list)-1, -1, -1):
    # print(i)
    if pass_flag:
        pass_flag = False
        continue
    # print("-----")
    if i == 0:
        break

    if a_list[i] == a_list[i-1]:
        pass_flag = True
        counter += 1
        continue
print(counter)
