N, M = map(int, input().split())
C_list = list(map(str, input().split()))
D_list = list(map(str, input().split()))
P_list = list(map(int, input().split()))

dic = dict()
extra_color = P_list[0]
for i in range(M):
    dic[D_list[i]] = P_list[i+1]

total = 0
for dish in C_list:
    if dish not in dic:
        total += extra_color
        continue
    total+= dic[dish]

print(total)
