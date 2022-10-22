H, W = map(int, input().split())
C_list = []
for _ in range(H):
    temp = input().split()
    C_list.append(temp)

result = []
for i in range(W):
    temp = []
    for j in C_list:
        temp.append(j[0][i])
    result.append(temp)
# print(result)

x = []
for i in result:
    # print(i)
    x.append(i.count('#'))


for num in x:
    print(num, end=" ")
