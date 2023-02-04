"""
#str型で受け取るとき
s = input()
#int型で受け取るとき
s = int(input())

A, B = map(int, input().split())

l = list(map(int, input().split()))
"""
N, K = map(int, input().split())
s_list = []
for i in range(N):
    s = input()
    s_list.append(s)

temp = s_list[:K]
temp.sort()
for i in temp:
    print(i)
