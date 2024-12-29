import math
N = int(input())
temp = set()

for i in range(1, int(math.sqrt(N))+1):
    if N % i == 0:
        temp.add(i)
        temp.add(N//i)

temp = list(temp)
temp.sort()

for i in temp:
    print(i)

