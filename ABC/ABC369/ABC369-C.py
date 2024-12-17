N = int(input())
A_list = list(map(int, input().split()))

if N == 1:
    print(1)
    exit()

if N == 2:
    print(3)
    exit()

diff = []
for i in range(len(A_list)-1):
    diff.append(A_list[i+1] - A_list[i])

temp = []
pre = diff[0]
count = 1
for i in range(1, len(diff)):
    if diff[i] == pre:
        count += 1
        if i == len(diff)-1:
            temp.append(count)
            break
        continue
    temp.append(count)
    count = 1
    pre = diff[i]
    if i == len(diff)-1:
        temp.append(count)
        break

result = len(A_list)

for i in temp:
    result += (((i+1)*i)//2)
    # print(result)

print(result)
