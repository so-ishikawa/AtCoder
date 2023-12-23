N, K = map(int, input().split())
A_list = list(map(int, input().split()))

sum_value = 0
if len(A_list) % 2 == 0:
    for i in range(0, len(A_list), 2):
        sum_value = abs(A_list[i] - A_list[i+1])
    print(sum_value)
    exit()

#odd
if len(A_list) == 1:
    print(0)
    exit()

pre_sum = []
suf_sum = []

for i in range(len(A_list)-1):
    diff = A_list[i+1] - A_list[i]
    

