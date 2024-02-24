N = int(input())
A_list = list(map(int, input().split()))

square_list_set = set([x*x for x in range(0, 200000)])
count = 0
for i in range(len(A_list)-1):
    for j in range(i+1, len(A_list)):
        if A_list[i]*A_list[j] in square_list_set:
            count += 1
print(count)
