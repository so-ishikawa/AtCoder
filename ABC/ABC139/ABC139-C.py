N = int(input())
H_list = list(map(int, input().split()))

count = 0
max_ = 0
for i in range(N-1):
    if H_list[i] >= H_list[i+1]:
        count += 1
        if count > max_:
            max_ = count
    else:
        count = 0
print(max_)
