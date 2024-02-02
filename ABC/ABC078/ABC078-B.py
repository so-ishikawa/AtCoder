X, Y, Z = map(int, input().split())

_X = X - 2*Z
count = 0
for i in range(1, 100000):
    if _X < Y*i + Z*(i-1):
        break
    count += 1

print(count)    
