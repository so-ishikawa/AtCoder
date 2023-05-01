# A, B = map(int, input().split())
# l = list(map(int, input().split()))
import copy

H, W = map(int, input().split())
A_list = []
for i in range(H):
    a = input()
    A_list.append(a)
B_list = []
for i in range(H):
    b = input()
    B_list.append(b)


for t in range(W):
    for s in range(H):
        temp = copy.copy(A_list)
        temp = temp[s:] + temp[:s]
        for i in range(H):
            temp[i] = temp[i][t:] + temp[i][:t]

        #確認
        flag = True
        for j in range(W):
            for i in range(H):
                if temp[i][j] != B_list[i][j]:
                    flag = False
                    break
            if not flag:
                break
        if flag:
            print("Yes")
            exit()
print("No")
        

