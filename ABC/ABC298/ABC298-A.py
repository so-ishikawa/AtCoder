"""
A, B = map(int, input().split())
#list型で取得
l = list(map(int, input().split()))
"""

N = int(input())
S = input()

if S.count("o") >= 1 and  S.count("x") == 0:
    print("Yes")
else:
    print("No")
