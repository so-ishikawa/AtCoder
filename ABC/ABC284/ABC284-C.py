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
    uv_list.append((v,u))

vertex_flag_list = [False] * N
vertex_flag_list.insert(0, None)

vertex_connection_dic = {}
for i in uv_list:
    if i[0] in vertex_connection_dic:
        vertex_connection_dic[i[0]].append(i[1])
    else:
        vertex_connection_dic[i[0]] = [i[1]]


# print(uv_list, vertex_flag_list, vertex_connection_dic)
counter = 0

def func(index):
    if vertex_flag_list[index] == True:
        return
    else:
        vertex_flag_list[index] = True
    if index not in vertex_connection_dic:
        return
    for i in vertex_connection_dic[index]:
        func(i)


for i in range(len(vertex_flag_list)):
    if vertex_flag_list[i] == None:
        continue
    if vertex_flag_list[i] == True:
        continue

    counter += 1
    func(i)
    """
    vertex_flag_list[i] = True
    if i not in vertex_connection_dic:
        continue
    for j in vertex_connection_dic[i]:
        func(j)
    """

print(counter)
