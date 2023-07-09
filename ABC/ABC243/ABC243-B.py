N = int(input())
A_list = list(map(int, input().split()))
B_list = list(map(int, input().split()))

A_set = set(A_list)
B_set = set(B_list)

A_B_intersection_set = A_set & B_set

answer_1_count = 0
for i in A_B_intersection_set:
    if A_list.index(i) == B_list.index(i):
        answer_1_count += 1

print(answer_1_count)
print(len(A_B_intersection_set) - answer_1_count)
