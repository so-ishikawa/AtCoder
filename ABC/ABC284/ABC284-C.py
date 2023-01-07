"""
#str型で受け取るとき
s = input()
#int型で受け取るとき
s = int(input())
# 入力が整数の時
A, B = map(int, input().split())
#list型で取得
l = list(map(int, input().split()))
"""



N, M = map(int, input().split())
uv_list = []

for i in range(M):
    u, v = map(int, input().split())
    uv_list.append((u,v))

connection_list = [[]]*N
connection_list.insert(0, None)

for i in uv_list:
    connection_list[i[0]].append(i[1])
    connection_list[i[1]].append(i[0])

flag_list = [-1]*N
flag_list.insert(0, None)

def X(root_index, target_index):
    if flag_list[target_index] != -1:
        return
    flag_list[target_index] = root_index
    for i in connection_list[target_index]:
        X(root_index, i)

# print(connection_list)
for i in connection_list:
    if i==None:
        continue
    for j in i:
        X(i, j)

print(flag_list)

# 途中
