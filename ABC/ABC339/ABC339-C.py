N = int(input())
A_list = list(map(int, input().split()))

min_value = 999999999999
temp = 0
for a in A_list:
    temp = temp + a
    if min_value > temp:
        min_value = temp

result = 0
if min_value >= 0:
    pass
else:
    result = -1 * min_value

print(result + sum(A_list))

