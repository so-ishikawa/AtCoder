N = int(input())

pre_value = 1
pre_pre_value = 2

if N == 1:
    print(1)
    exit()

for i in range(2, N+1):
    temp = pre_pre_value + pre_value
    pre_pre_value = pre_value
    pre_value = temp

    if i == N:
        print(temp)
        exit()


