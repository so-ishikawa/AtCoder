"""
#文字列として受け取るとき
A, B, C = input().split()

A, B = map(int, input().split())

#list型で取得
l = list(map(int, input().split()))
"""
N = int(input())
S = input()

if S.count("MM") == 0 and S.count("FF") == 0:
    print("Yes")
else:
    print("No")
