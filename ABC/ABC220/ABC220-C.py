N = int(input())
A_list = list(map(int, input().split()))
X = int(input())

num = X // sum(A_list)
remain = X % sum(A_list)


for i in range(len(A_list)):
    remain -= A_list[i]
    if remain < 0:
        print(num*len(A_list)+i+1)
        exit()
