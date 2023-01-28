"""
#str型で受け取るとき
s = input()
#int型で受け取るとき
s = int(input())

A, B = map(int, input().split())

#list型で受け取るとき
s = input().split()
"""
import sys

N, M = map(int, input().split())
set_1 = set([])
set_2 = set([])

for i in range(M):
    u, v = map(int, input().split())
    if u not in set_1:
        set_1.add(u)
    elif u not in set_2:
        set_2.add(u)
    else:
        print("No")
        sys.exit(0)
    if v not in set_1:
        set_1.add(v)
    elif v not in set_2:
        set_2.add(v)
    else:
        print("No")
        sys.exit(0)
if len(set_1 - set_2) != 2:
    print("No")
    sys.exit(0)

if N - len(set_2) != 2:
    print("No")
    sys.exit(0)

if N != len(set_1):
    print("No")
    sys.exit(0)

print("Yes")

