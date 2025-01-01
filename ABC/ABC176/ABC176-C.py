N = int(input())
A_list = list(map(int, input().split()))

diff = A_list[0]
sum_ = 0

for i in A_list:
    if i < diff:
        sum_ += (diff-i)
    else:
        diff = i
print(sum_)
