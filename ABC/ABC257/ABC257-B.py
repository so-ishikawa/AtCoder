N, K, Q = map(int, input().split())
A_list = list(map(int, input().split())) #len = K
L_list = list(map(int, input().split())) #len = Q

temp = ["dummy"] + A_list
for i in L_list:
    if temp[i] == N:
        continue
    if len(temp) > i+1 and temp[i] + 1 == temp[i+1]:
        continue
    temp[i] = temp[i] + 1

for i in range(1, len(temp)):
    print(temp[i], end=" ")
