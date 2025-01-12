N = int(input())
A_list = list(map(int, input().split()))

# result_set = set()
count = 0
check_set = set()
check_set_inner = set()

for i in range(N-1):
    if A_list[i] in check_set:
        continue
    check_set.add(A_list[i])
    check_set_inner.clear()
    for j in range(i+1, N):
        if A_list[j] in check_set_inner:
            continue
        check_set_inner.add(A_list[j])

        if A_list[i] == A_list[j]:
            continue
        # result_set.add((i,j))
        count += 1
print(count)
