"""
#str型で受け取るとき
s = input()
#int型で受け取るとき
s = int(input())

A, B = map(int, input().split())

l = list(map(int, input().split()))
"""


s = int(input())

a_list = []
b_list = []
for i in range(s):
    A, B = map(int, input().split())
    print(A+B)




