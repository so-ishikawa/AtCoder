N = int(input())
a_list = list(map(int, input().split()))
pre_list = a_list.copy()

for i in range(N-1): #段数
    temp_list = [0] * N
    for j in range(N): # 横行升目
        sum_ = 0
        for index in range(max(0, j-1), min(N-1, j+1)+1):
            sum_ += pre_list[index]
        temp_list[j] = sum_ % 100
    pre_list = temp_list.copy()
print(pre_list[N-1])
