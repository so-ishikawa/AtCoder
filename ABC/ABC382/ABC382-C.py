N, M = map(int, input().split())
A_list = list(map(int, input().split()))
B_list = list(map(int, input().split()))


# for a in A_list:
for b in B_list:
    flag = False
    for a_num in range(len(A_list)):
        a = A_list[a_num]
        if b >= a:
            print(a_num+1)
            flag = True
            break
    if not flag:
        print(-1)
