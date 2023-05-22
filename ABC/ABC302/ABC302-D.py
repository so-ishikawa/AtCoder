N, M, D = map(int, input().split())
A_list = list(map(int, input().split()))
B_list = list(map(int, input().split()))

A_set = set(A_list)
B_set = set(B_list)

existence_list = A_list + B_list
existence_list.sort(reverse=True)

for i in range(len(existence_list)):
    for j in range(i, len(existence_list)):
        if existence_list[i] - existence_list[j] > D:
            break
        if existence_list[i] in A_set and existence_list[j] in B_set or existence_list[i] in B_set and existence_list[j] in A_set:
            print(existence_list[i] + existence_list[j])
            exit()
print(-1)

