N, X = map(int, input().split())
A_list = list(map(int, input().split()))

for i in range(0, 100+1):
    A_list_copy = A_list.copy()
    A_list_copy.append(i)

    A_list_copy.sort()
    if sum(A_list_copy[1:-1]) >= X:
        # print(A_list[1:-1])
        print(i)
        exit()
print(-1)
exit()
