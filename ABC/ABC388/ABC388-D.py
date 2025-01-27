N = int(input())
A_list = list(map(int, input().split()))

diff_list = [0]*N
for i in range(len(A_list)):
    diff_list[i+1] = diff_list[i+1] + 1
    if i+1+A_list[i] < len(A_list):
        diff_list[i+1+A_list[i]] = diff_list[i+1+A_list[i]] - 1

for i in range(len(A_list)):
    A_list
