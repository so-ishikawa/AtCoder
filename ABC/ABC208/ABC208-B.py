import math
P = int(input())

coin_list = []
for i in range(1, 10+1):
    coin_list.insert(0, math.factorial(i))

count = 0
for i in coin_list:
    if P == 0:
        break
    count = count + (P // i)
    P = P % i

print(count)
