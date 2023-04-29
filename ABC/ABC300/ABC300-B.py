# A, B = map(int, input().split())
# l = list(map(int, input().split()))
import copy
H, W = map(int, input().split())
A_list = []
for i in range(H):
    w = input()# list(map(int, input().split()))
    A_list.append(w)
B_list = []
for i in range(H):
    w = input()# list(map(int, input().split()))
    B_list.append(w)

# Aを操作してBになるかを考える
# まずは縦
tate_flag = False
yoko_flag = False

AA_list = copy.copy(A_list)
for m in range(H):
    for n in range(H):
        if B_list[n].count("#") != A_list[n].count("#"):
            continue
        if n == H-1:
            tate_flag = True
    if not tate_flag:
        temp = A_list.pop(0)
        A_list.append(temp)
    
    # if m == H-1 and tate_flag == False:
    #     print("No")
    #     exit()


    for _ in range(W):
        temp_flag = True
        for n_ in range(W):
            for k in range(H):
                if A_list[k][n_] != B_list[k][n_]:
                    temp_flag = False
                    break

        if temp_flag:
            print("Yes")
            exit()
    
        for o in range(H):
            temp = A_list[o][1:]
            A_list[o] = temp+A_list[o][0]

    A_list = copy.copy(AA_list)
print("No")




