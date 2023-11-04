# import math
B = int(input())

if B == 1:
    print(1)
    exit()

for i in range(1000):
    if i**i == B:
        print(i)
        exit()
print(-1)
