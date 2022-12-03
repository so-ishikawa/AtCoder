n = int(input())
s_list = list(map(int, input().split()))

temp = 0
result = []
for i in range(len(s_list)):
    if i == 0:
        temp = s_list[i]
        # print(s_list[i])
        result.append(s_list[i])
        continue
    result.append(s_list[i] - temp)
    # print(s_list[i] - temp)
    temp = s_list[i]

for i in result:
    print(i , end=' ')

