N = int(input())
A_list = list(map(int, input().split()))
Q = int(input())
query_list = []
for i in range(Q):
    query_list.append(list(map(int, input().split())))

for i in query_list:
    if i[0] == 1:
        A_list[i[1] - 1] = i[2]
    else:
        print(A_list[i[1] -1])

