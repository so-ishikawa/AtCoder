N, M = map(int, input().split())
A_list = list(map(int, input().split()))
B_list = list(map(int, input().split()))

A_list.insert(0, "dummy")
B_list.insert(0, "dummy")

# result_flag = False
L = int("1"*N, 2)

for i in range(0, L+1):

    temp = format(i, "b")
    temp = temp.rjust(N, "0")
    temp = "_" + temp #add dummy
    
    for m in range(1, M+1):
        if temp[A_list[m]] == temp[B_list[m]]:
            break
        if m == M:
            # result_flag = True
            print("Yes")
            exit()


print("No")
