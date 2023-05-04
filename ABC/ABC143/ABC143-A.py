A, B = map(int, input().split())
temp = A - 2*B
if temp <= 0:
    print(0)
else:
    print(temp)