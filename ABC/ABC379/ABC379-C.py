N, M = map(int, input().split())
X_list = list(map(int, input().split()))
A_list = list(map(int, input().split()))

dic = dict()
for x_index in range(len(X_list)):
    dic[X_list[x_index]] = A_list[x_index]

X_list.sort()
    
if sum(A_list) != N:
    print(-1)
    exit()

temp_count = 0
x_count = 0
for i in range(1, N+1):
    if i in dic:
        x_count += (dic[i]-1)
        continue
    temp_count = temp_count + 1

    if temp_count > x_count:
        print(-1)
        exit()


