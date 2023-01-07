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

result_list = [None]
for i in range(N):
    result_list.append(i+1)

for i in uv_list:
    result_list[i[1]] = i[0]

for i in range(len(result_list)-1, 0, -1):
    temp_index = result_list[i]
    while True:
        if temp_index == result_list[temp_index]:
            result_list[i] = temp_index
            break
        temp_index = result_list[temp_index]

print(len(set(result_list))-1)
