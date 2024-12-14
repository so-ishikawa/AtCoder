N, S = map(int, input().split())
A_list = list(map(int, input().split()))

sum_ = sum(A_list)
target = S % sum_

prefix_sum = set()
temp = 0
for i in (A_list + A_list):
    temp = temp + i
    prefix_sum.add(temp)

for i in prefix_sum:
    if (i + target) in prefix_sum:
        print("Yes")
        exit()
print("No")
