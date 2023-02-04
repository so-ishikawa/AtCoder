"""
#str型で受け取るとき
s = input()
#int型で受け取るとき
s = int(input())

A, B = map(int, input().split())

l = list(map(int, input().split()))
"""

N, M = map(int, input().split())
a_list = []
b_list = []
for i in range(M):
    A, B = map(int, input().split())
    a_list.append(A)
    b_list.append(B)

