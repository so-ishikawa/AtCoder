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

N = int(input())
s_list = []
for i in range(N):
    s = input()
    s_list.append(s)

for i in range(len(s_list)-1, -1, -1):
    print(s_list[i])
