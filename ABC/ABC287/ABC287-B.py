"""
#str型で受け取るとき
s = input()
#int型で受け取るとき
s = int(input())

A, B = map(int, input().split())

#list型で受け取るとき
s = input().split()
"""
N, M = map(int, input().split())
s_list = []
t_list = []
for i in range(N):
    s = int(input())
    s_list.append(s)
for i in range(M):
    t = int(input())
    t_list.append(t)

count = 0
for i in range(N):
    temp = s_list[i] % 1000
    if temp in t_list:
        count += 1

print(count)
