N = int(input())
S_list = []
for i in range(1, N+1):
    S_list.append((i, input().count("o")))

S_list.sort(key=lambda x: (-x[1], x[0]))
for i in S_list:
    print(i[0], end=" ")
