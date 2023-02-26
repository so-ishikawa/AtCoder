"""
#str型で受け取るとき
s = input()
#int型で受け取るとき
s = int(input())
A, B = map(int, input().split())
#list型で取得
l = list(map(int, input().split()))
"""
import sys
N = int(input())
S = input()

check_set = set()
temp_x = 0
temp_y = 0
check_set.add((0,0))

for i in S:
    if i == "R":
        temp_x += 1
    elif i=="L":
        temp_x -= 1
    elif i=="U":
        temp_y += 1
    else:
        temp_y -= 1
    if (temp_x, temp_y) in check_set:
        print("Yes")
        sys.exit(0)
    check_set.add((temp_x, temp_y))
print("No")
