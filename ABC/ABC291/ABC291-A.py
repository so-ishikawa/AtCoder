"""
#str型で受け取るとき
s = input()
#int型で受け取るとき
s = int(input())
A, B = map(int, input().split())
#list型で取得
l = list(map(int, input().split()))
"""

S = input()
counter = 0
for i in S:
    if i.isupper():
        print(counter+1)
    counter += 1










