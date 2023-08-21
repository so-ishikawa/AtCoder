N = int(input())
A_list = list(map(int, input().split()))

max_gcd_num = 0
max_index = 0

A_list.sort()

for i in range(2, A_list[-1]+1):
    temp = len([x for x in A_list if x % i == 0])
    if max_gcd_num < temp:
        max_gcd_num = temp
        max_index = i

print(max_index)
