"""
A, B = map(int, input().split())
#list型で取得
l = list(map(int, input().split()))
"""
Q = int(input())
query_list = []
for i in range(Q):
    l = list(map(int, input().split()))
    query_list.append(l)

S = [1]
delete_count = 0
for query in query_list:
    if query[0] == 1:
        # S = S + str(query[1])
        S.append(query[1])
    elif query[0] == 2:
        delete_count += 1
    else: #3
        temp = 0
        for i in range(delete_count, len(S)):
            temp = temp * 10 + S[i]
        print(temp% 998244353)
