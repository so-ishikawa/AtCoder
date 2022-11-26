import math

a, b = map(int, input().split())
best_time = 999999999999999999
# a =  10

# b =  1
for i in range(10000):
    temp = i*b + a / math.sqrt(i + 1)
    if temp < best_time:
        best_time = temp
print(best_time)
