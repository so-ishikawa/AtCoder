"""
A, B = map(int, input().split())
#list型で取得
l = list(map(int, input().split()))
"""



N = int(input())
left = 1
right = N
while left + 1 < right:
    mid = (left + right)//2
    print("?", mid)
    s = int(input())
    if s == 0:
        left = mid
    else:
        right = mid
print("!", left)
