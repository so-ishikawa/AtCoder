import bisect

N = int(input())
A_list = list(map(int, input().split()))

sum_ = 0
for a in A_list:
    index = bisect.bisect_left(A_list, 2*a)
    if index == len(A_list):
        break
    sum_ += (len(A_list)-index)
print(sum_)
