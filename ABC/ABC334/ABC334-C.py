N, K = map(int, input().split())
A_list = list(map(int, input().split()))

if K % 2 == 0: #even
    sum_ = 0
    for i in range(len(A_list)//2):
        sum_ += abs(A_list[i] - A_list[i+1])
    print(sum_)
    exit()

# odd
even_dict = dict()
odd_dict = dict()

for i in range(1, len(A_list), 2):
    even_dict[i] = abs(A_list[i] - A_list[i+1])
for i in range(0, len(A_list)-1, 2):
    odd_dict[i] = abs(A_list[i] - A_list[i+1])
# print(even_dict, odd_dict)
min_value = 999999999999999999999999999

for i in range(0, len(A_list), 2):
    lhs = [x for x in odd_dict.keys() if i > x]
    temp = 0
    for j in lhs:
        temp += odd_dict[j]
    rhs = [x for x in even_dict.keys() if i < x]
    # print(i, lhs, rhs)
    for j in rhs:
        temp += even_dict[j]
    if min_value > temp:
        min_value = temp
print(min_value)
