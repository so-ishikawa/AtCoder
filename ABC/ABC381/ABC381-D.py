N = int(input())
A_list = list(map(int, input().split()))

flag_list = [False] * len(A_list)

for i in range(N-1):
    if A_list[i] == A_list[i+1]:
        flag_list[i] = True

# even
check_set = set()
best_count = 0
for i in range(0, N-1, 2):
    if not flag_list[i]:
        check_set.clear()
        continue

    if A_list[i] not in check_set:
        check_set.add(A_list[i])
        if best_count < len(check_set)*2:
            best_count = len(check_set)*2
        continue

    # A_list[i] in check_set
    for j in range(i-len(check_set)*2, i, 2):
        if A_list[i] in check_set:
            check_set.remove(A_list[j])

        if A_list[i] not in check_set:
            check_set.add(A_list[i])
            break

#odd
check_set.clear()

for i in range(1, N-1, 2):
    if not flag_list[i]:
        check_set.clear()
        continue

    if A_list[i] not in check_set:
        check_set.add(A_list[i])
        if best_count < len(check_set)*2:
            best_count = len(check_set)*2
        continue

    # A_list[i] in check_set
    for j in range(i-len(check_set)*2, i, 2):
        if A_list[i] in check_set:
            check_set.remove(A_list[j])

        if A_list[i] not in check_set:
            check_set.add(A_list[i])
            break

print(best_count)
