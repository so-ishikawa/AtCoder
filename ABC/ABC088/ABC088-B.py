N = int(input())
a_list = list(map(int, input().split()))
a_list.sort(reverse=True)

lhs = []
rhs = []

for a_index in range(len(a_list)):
    if a_index % 2 == 0:
        lhs.append(a_list[a_index])
        continue
    rhs.append(a_list[a_index])

print(sum(lhs)-sum(rhs))
