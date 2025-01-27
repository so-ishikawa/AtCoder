import math
R = int(input())

if R < math.sqrt(2)/2:
    print(0)
    exit()

axis_num = int(math.sqrt(R*R-1/4) - 1/2)

count = 0

for i in range(1, axis_num+1):
    count += int(math.sqrt(R*R - (1/2+i)**2) - 1/2)

print(axis_num*4 + 1 + count*4)
