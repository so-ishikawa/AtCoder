N, M, L = map(int, input().split())
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))

ng_list = set()
for i in range(L):
    c, d = map(int, input().split())
    ng_list.add((c-1,d-1))

a_list_with_index = []
for i in range(len(a_list)):
    a_list_with_index.append((i, a_list[i]))

b_list_with_index = []
for i in range(len(b_list)):
    b_list_with_index.append((i, b_list[i]))

a_list_with_index.sort(key=lambda x: x[1], reverse=True)
b_list_with_index.sort(key=lambda x: x[1], reverse=True)

max_value = 0
for a in a_list_with_index:
    for b in b_list_with_index:
        if (a[0], b[0]) in ng_list:
            continue
        max_value = max(max_value, a[1]+b[1])
        break
print(max_value)

