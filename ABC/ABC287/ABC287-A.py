"""
#str型で受け取るとき
s = input()
#int型で受け取るとき
s = int(input())

A, B = map(int, input().split())

#list型で受け取るとき
s = input().split()
"""
N = int(input())
s_list = []
for i in range(N):
    s = input()
    s_list.append(s)
if s_list.count("For") > N//2:
    print("Yes")
else:
    print("No")
