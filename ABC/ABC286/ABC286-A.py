N, P, Q, R, S = map(int, input().split())
A_list = list(map(int, input().split()))

A_list.insert(0, "dummy")
a = A_list[P:Q+1]
b = A_list[R:S+1]
A_list[P:Q+1] = b
A_list[R:S+1] = a
A_list.pop(0)
for i in A_list:
    print(i, end=" ")
