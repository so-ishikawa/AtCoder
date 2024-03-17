N, M = map(int, input().split())
A_list = list(map(int, input().split()))

masu = [0]*N

for i in range(1, N):
    min_value = 99999999999
    for j in range(1, M+1):
        if i - j < 0:
            break
        temp_value = masu[i-j] + j*A_list[i]
        if min_value > temp_value:
            min_value = temp_value
    masu[i] = min_value
print(masu[-1])
