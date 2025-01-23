import math

N = int(input())
a_list = list(map(int, input().split()))
a_list.insert(0, "dummy")

order = 0
r_order = 0

for i in range(1, len(a_list)):
    if i == a_list[i]:
        order += 1
    elif i == a_list[a_list[i]]:
        r_order += 1

print(math.comb(order, 2) + r_order//2)
