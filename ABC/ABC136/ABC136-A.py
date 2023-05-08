A, B, C = map(int, input().split())
temp = A - B
temp2 = 0 if C - temp <= 0 else C - temp
print(temp2)
