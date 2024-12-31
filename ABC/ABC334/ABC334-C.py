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

temp = 0
for i in range(1, len(A_list), 2):
    temp += (abs(A_list[i] - A_list[i+1]))
    even_dict[i] = temp

for i in range(0, len(A_list)-1, 2):
    odd_dict[i] = abs(A_list[i] - A_list[i+1])
temp = 0
a = list(odd_dict.keys())
a.sort(reverse=True)
for i in a:
    temp += odd_dict[i]
    odd_dict[i] = temp

min_value = 999999999999999999999999999

for i in range(0, len(A_list), 2):
    temp = 0
    b = [x for x in even_dict.keys() if i > x]
    if len(b) > 0:
        temp += even_dict[max(b)]
    # print(i, temp, "?")
    b = [x for x in odd_dict.keys() if i < x]
    # print(b, ">>>")
    if len(b) > 0:
        temp += odd_dict[min(b)]
    # print(i, temp, "!")
    if min_value > temp:
        min_value = temp
print(min_value)
