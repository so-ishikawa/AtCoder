N, D = map(int, input().split())
X_list = []
for i in range(N):
    X_list.append(list(map(int, input().split())))

d_num = len(X_list[0])
# print(X_list)
counter = 0
for y in range(N-1):
    for z in range(y+1, N):
        # print(y,z)
        temp = 0
        for i in range(d_num):
            # print(y,z,i)
            temp += (X_list[y][i] - X_list[z][i])**2
        temp = temp ** (1/2)
        if temp.is_integer():
            # print(y,z,temp)
            counter += 1
print(counter)
