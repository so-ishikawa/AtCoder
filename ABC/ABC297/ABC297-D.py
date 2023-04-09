"""
A, B = map(int, input().split())
#list型で取得
l = list(map(int, input().split()))
"""
A, B = map(int, input().split())
if A < B:
    temp = A
    A = B
    B = temp

count = 0

while B != 0:
    count  = count +  A // B
    A = A % B
    temp = A
    A = B
    B = temp

print(count-1)

