"""
A, B = map(int, input().split())
#list型で取得
l = list(map(int, input().split()))
"""
N = int(input())
A_list = []
for i in range(N):
    l = list(map(int, input().split()))
    A_list.append(l)

B_list = []
for i in range(N):
    l = list(map(int, input().split()))
    B_list.append(l)

temp_list = []
for i in range(N):
    l = [-1]*N
    temp_list.append(l)

temp2_list = []
for i in range(N):
    l = [-1]*N
    temp2_list.append(l)

temp3_list = []
for i in range(N):
    l = [-1]*N
    temp3_list.append(l)


# --------------------

flag = True
for i in range(N):
    for j in range(N):
        if A_list[i][j] == 1:
            if B_list[i][j] != 1:
                flag = False
                break
    if not flag:
        break
if flag:
    print("Yes")
    exit()

#----------------------
for i in range(N):
    for j in range(N):
        # print(N-1-j,i, temp_list,"!!")
        # temp_list[N-1-j][i] = A_list[i][j]
        temp_list[i][j] = A_list[N-1-j][i]
flag = True
for i in range(N):
    for j in range(N):
        if temp_list[i][j] == 1:
            if B_list[i][j] != 1:

                flag = False
                break
    if not flag:
        break
if flag:
    print("Yes")
    exit()
# print(temp_list)
#----------------------
for i in range(N):
    for j in range(N):
        # temp2_list[N-1-j][i] = temp_list[i][j]
        temp2_list[i][j] = temp_list[N-1-j][i]

flag = True
for i in range(N):
    for j in range(N):
        if temp2_list[i][j] == 1:
            if B_list[i][j] != 1:
                # print(B_list, temp2_list)
                flag = False
                break
    if not flag:
        break
if flag:
    print("Yes")
    exit()
# print(temp2_list)
#----------------------
for i in range(N):
    for j in range(N):
        # temp3_list[N-1-j][i] = temp2_list[i][j]
        temp3_list[i][j] = temp2_list[N-1-j][i]

flag = True
for i in range(N):
    for j in range(N):
        if temp3_list[i][j] == 1:
            if B_list[i][j] != 1:
                flag = False
                break
    if not flag:
        break
if flag:
    print("Yes")
    exit()

print("No")
