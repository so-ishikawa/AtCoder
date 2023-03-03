N, M = map(int, input().split())
a_list = list(map(int, input().split()))


cell_value = [0] * N * 2

for i in range(1, N):
    best_time = 9999999
    for j in range(1, M+1):
        if i-j < 0:
            continue
        temp_time = j * a_list[i]
        temp_time = cell_value[i-j] + temp_time
        if best_time > temp_time:
            best_time = temp_time
    cell_value[i] = best_time
print(cell_value[N-1])
