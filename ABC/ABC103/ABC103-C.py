import math
N = int(input())
list_a = list(map(int, input().split()))

"""
for test_value in range(100):
    temp = 0
    for i in list_a:
        temp += (test_value%i)
    print(test_value, ":" ,temp, "!!!")
"""
m = math.lcm(*list_a) - 1
# print(m)
temp = 0
for i in list_a:
    temp += (m%i)
    # print(temp)
print(temp)
    

