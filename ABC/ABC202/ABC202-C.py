N = int(input())
A_list = list(map(int, input().split()))
B_list = list(map(int, input().split()))
C_list = list(map(int, input().split()))

B_dic = dict()
for i in range(len(B_list)):
    B_dic.setdefault(B_list[i], []).append(i+1)

C_dic = dict()
for i in C_list:
    C_dic[i] = C_dic.get(i, 0) + 1

B_dic_C = dict()
for i in B_dic.keys():
    temp = 0
    for j in B_dic[i]:
        if j in C_dic:
            temp += C_dic[j]
    B_dic_C[i] = temp
count = 0
for i in A_list:
    if i in B_dic_C:
        count += B_dic_C[i]
print(count)

