N, K = map(int, input().split())
A_list = list(map(int, input().split()))

if K % 2 == 0: #even
    sum_ = 0
    for i in range(0, len(A_list), 2):
        sum_ += abs(A_list[i] - A_list[i+1])
    print(sum_)
    exit()

# odd
pre_dict = dict()
aft_dict = dict()

temp = 0
for i in range(0, len(A_list)-1, 2):
    temp += abs(A_list[i]-A_list[i+1])
    pre_dict[i+1] = temp

temp = 0
for i in range(len(A_list)-1, 1, -2):
    temp += abs(A_list[i]-A_list[i-1])
    aft_dict[i-1] = temp
# print(pre_dict, aft_dict)
min_value = 999999999999999999999999999999999999

for i in range(0, len(A_list), 2):
    sum_ = 0
    if i-1 in pre_dict:
        sum_ += pre_dict[i-1]
    if i+1 in aft_dict:
        sum_ += aft_dict[i+1]

    if min_value > sum_:
        min_value = sum_

print(min_value)
