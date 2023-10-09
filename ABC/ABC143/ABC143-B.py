N = int(input())
d_list = list(map(int, input().split()))

sum_ = 0
for i in range(N-1):
    for j in range(i+1, N):
        sum_ += d_list[i]*d_list[j]
print(sum_)
